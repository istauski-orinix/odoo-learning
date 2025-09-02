from odoo import models, fields

class LibraryRental(models.Model):
    _name = 'library.rental'
    _description = 'Library Book Rental'
    book_id = fields.Many2one(
        'library.book',
        string='Book',
        required=True,
        ondelete='cascade'
    )
    _inherits = {'library.book': 'book_id'}

    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    rental_date = fields.Date(string='Rental Date', default=fields.Date.today)
    return_date = fields.Date(string='Return Date')
    state = fields.Selection([
        ('ongoing', 'Ongoing'),
        ('returned', 'Returned'),
    ], string='State', default='ongoing', required=True)

