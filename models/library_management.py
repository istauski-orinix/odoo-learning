from odoo import fields, models, api
import logging
import requests

_logger = logging.getLogger(__name__)

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _rec_names_search = ['title']

    title = fields.Char(string='Book Name', required=True)
    author = fields.Char(string='Author', required=True)
    isbn = fields.Char(string='ISBN')
    genres = fields.Many2many('library.genre', string='Genre')
    description = fields.Text(string='Description', compute='_compute_state')
    page_number = fields.Integer(string='Page Number')
    published_date = fields.Date(string='Published Date')
    reading_progress = fields.Float(string='Reading Progress', default=1.0)
    archived_date = fields.Date(string='Archived Date')
    publisher_id = fields.Many2one('library.publisher', string='Publisher', required=True)
    state = fields.Selection([('draft', 'Draft'),('archived', 'Archived'), ('else', 'Else'),
                              ('available', 'Available'), ('featured', 'Featured')], string='Status')
    cover_image = fields.Image(string='Cover Image')
    borrowing_id = fields.One2many('library.book.wizard', 'book_id', string='Book')
    is_available = fields.Boolean(string='Is Available', required=True)
    is_hefty = fields.Boolean(string='Is Hefty', compute='_compute_is_hefty')
    full_title = fields.Char(string='Full Title', compute='_compute_full_name', store=True)
    borrower_email = fields.Char(string='Borrower Email', default='example@mail.com')

    _sql_constraints = [
        (
            'full_title_uniqueness',
            'unique(full_title)',
            'Book full title is duplicated somewhere'
        ),
        (
            'date_viable',
            'CHECK(published_date <= archived_date)',
            'Wrong date for book, archived date must be after or on published date'
        ),
    ]

    @api.depends('title', 'author')
    def _compute_full_name(self):
        for book in self:
            if book.title and book.author:
                book.full_title = f"{book.title} - {book.author}"
            else:
                book.full_title = book.title or ''

    @api.depends('page_number')
    def _compute_is_hefty(self):
        for book in self:
            if book.page_number > 300:
                book.is_hefty = True
            else:
                book.is_hefty = False

    @api.onchange('state')
    def _compute_state(self):
        for book in self:
            if book.state == 'archived':
                book.description = 'O_O'
            else:
                book.description = '!!!'

    def action_mark_as_featured(self):
        for book in self:
            if book.state == 'draft':
                book.state = 'featured'

    def action_mark_as_archived(self):
        for book in self:
            if book.state == 'draft':
                book.state = 'archived'

    @api.model
    def auto_reading(self):
        _logger.info("CRON JOB: 'Auto read books' is running...")
        featured_books = self.search([('state', '=', 'featured')])
        for book in featured_books:
            if book.reading_progress < 100.0:
                book.reading_progress += 3.0
            if book.reading_progress >= 100.0:
                book.state = 'available'

    def action_fetch_book_data(self):
        records = self.search([('isbn', '!=', '')])

        for record in records:
            try:
                isbn = record.isbn
                url = f"https://openlibrary.org/books/{isbn}.json"
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                data = response.json()
                _logger.info(f"Book: {data}")

                if data:
                    record.page_number = data['number_of_pages']
                    record.title = data['title']
                else:
                    _logger.warning("No results found for isbn %s", record.isbn)

            except requests.exceptions.RequestException as e:
                _logger.error("Error fetching geocode data: %s", e)

    def action_send_book_email(self):
        template_id = self.env.ref('library_module.email_template_borrow_reminder')
        for record in self:
            if template_id:
                template_id.send_mail(record.id, force_send=True)