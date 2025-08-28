from odoo import models, fields

class LibraryPublisher(models.Model):
    _name = 'library.publisher'
    _description = 'Library Publisher'

    name = fields.Char(string='Publisher', required=True)
    books = fields.One2many('library.book', 'publisher_id', string='Books')