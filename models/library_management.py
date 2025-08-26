from odoo import fields, models

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string='Book Name', required=True)
    author = fields.Char(string='Author', required=True)
    ISBN = fields.Char(string='ISBN', required=True)
    description = fields.Text(string='Description', required=True)
    published_date = fields.Date(string='Published Date', required=True)
    publisher = fields.Many2one('library.publisher', string='Publisher', required=True)
    is_available = fields.Boolean(string='Is Available', required=True)

class LibraryPublisher(models.Model):
    _name = 'library.publisher'
    _description = 'Library Publisher'

    name = fields.Char(string='Publisher', required=True)