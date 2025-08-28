from odoo import models

class LibraryCatalog(models.Model):
    _inherit = 'library.book'

    def _compute_full_name(self):
        res = super(LibraryCatalog, self)._compute_full_name()
        res = f"{self.title} + {self.author} -- COOOOL"
        self.full_title = res