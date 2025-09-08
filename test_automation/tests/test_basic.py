from odoo.tests.common import TransactionCase


class TestBasic(TransactionCase):

    def test_sample_always_pass(self):
        self.assertTrue(True, "This test always passes.")

    def test_string_concatenation(self):
        result = "Hello" + " " + "World"
        self.assertEqual(result, "Hello World")

    def test_error_showcase(self):
        self.assertTrue(False, "This error test showcase.")
