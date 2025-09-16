from odoo import models, fields


class StoreContact(models.Model):
    _name = "store.contact"
    _description = "Store Contact Message"

    name = fields.Char(required=True)
    message = fields.Text()
    create_date = fields.Datetime(readonly=True)
