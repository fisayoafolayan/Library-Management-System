import unittest
import utilities


class TestUtilities(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = utilities.InputValidator()

    def test_validate_data_type_returns_true_for_valid_input(self):
        self.assertTrue(self.validator.validate_data_type('data', 'string'))

    def test_validate_data_type_raises_error_for_invalid_input(self):
        self.assertFalse(self.validator.validate_data_type(234, 'string'))
