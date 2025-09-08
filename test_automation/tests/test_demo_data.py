from odoo.tests.common import TransactionCase


class TestDemoData(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(TestDemoData, cls).setUpClass()
        cls.partner_model = cls.env["res.partner"]

    def test_demo_partners(self):
        partner_count = self.partner_model.search_count([("email", "ilike", "partner")])
        self.assertTrue(partner_count >= 2, "Demo data count is valid")
