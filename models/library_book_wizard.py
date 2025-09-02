from odoo import fields, models

class LibraryBookWizard(models.TransientModel):
    _name = 'library.book.wizard'
    _description = 'Library Book Wizard'

    book_id = fields.Many2one('library.book', string='Book')
    borrow_date = fields.Date(string='Due Date')
    borrower_email = fields.Char(string='Borrower Email')

    def action_confirm_borrow(self):
        self.book_id.state = 'featured'
        self.book_id.borrower_email = self.borrower_email