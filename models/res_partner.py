from odoo import fields, models

class LibraryResPartner(models.Model):
    _inherit = 'res.partner'

    membership_id = fields.Integer(string='Membership ID')