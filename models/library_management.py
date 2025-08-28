from odoo import fields, models, api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string='Book Name', required=True)
    author = fields.Char(string='Author', required=True)
    isbn = fields.Char(string='ISBN')
    genres = fields.Many2many('library.genre', string='Genre')
    description = fields.Text(string='Description', compute='_compute_state')
    page_number = fields.Integer(string='Page Number')
    published_date = fields.Date(string='Published Date')
    reading_progress = fields.Float(string='Reading Progress', default=0.2)
    archived_date = fields.Date(string='Archived Date')
    publisher_id = fields.Many2one('library.publisher', string='Publisher', required=True)
    state = fields.Selection([('draft', 'Draft'),('archived', 'Archived'), ('else', 'Else'),
                              ('available', 'Available'), ('featured', 'Featured')], string='Status')
    cover_image = fields.Image(string='Cover Image')
    is_available = fields.Boolean(string='Is Available', required=True)
    is_hefty = fields.Boolean(string='Is Hefty', compute='_compute_is_hefty')
    full_title = fields.Char(string='Full Title', compute='_compute_full_name', store=True)

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