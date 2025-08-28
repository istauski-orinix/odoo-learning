from odoo import fields, models

class LibraryGenre(models.Model):
    _name = 'library.genre'

    name = fields.Char(string='Genre', required=True)