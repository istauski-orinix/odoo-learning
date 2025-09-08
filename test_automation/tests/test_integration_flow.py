from odoo.tests.common import TransactionCase


def test_create_and_confirm_model(self):
    test_model = self.env["test.model"].create(
        {
            "name": "Integration Test Record",
        }
    )
    test_model.action_confirm()
    self.assertEqual(
        test_model.state, "confirmed", "The record should be in confirmed state."
    )
