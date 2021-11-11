import unittest
from Model.users import Users


class TestUsers(unittest.TestCase):

    # initial setup to test user class
    def setUp(self) -> None:
        self.first_user = {
            'username': 'friday',
            'firstname': 'Friday',
            'surname': 'Friday',
            'street_name': 'Yaba',
            'house_number': 25,
            'postcode': 2554,
            'email_address': 'tester@test.com',
            'date_of_birth': '02-05-97',
        }
        self.users = Users(**self.first_user)

    # Method to get username
    def test_get_username(self):
        self.assertEqual(self.users.get_username(), self.first_user['username'])

    # Method to set username
    def test_set_username(self):
        new_data = 'new_username'
        self.users.set_username(new_data)
        self.assertNotEqual(self.users.get_username(), self.first_user['username'])
        self.assertEqual(self.users.get_username(), new_data)

    # Method to get username
    def test_get_firstname(self):
        self.assertEqual(self.users.get_firstname(), self.first_user['firstname'])

    # Method to set firstname
    def test_set_firstname(self):
        new_data = 'new_firstname'
        self.users.set_firstname(new_data)
        self.assertNotEqual(self.users.get_firstname(), self.first_user['firstname'])
        self.assertEqual(self.users.get_firstname(), new_data)

    # Method to get surname
    def test_get_surname(self):
        self.assertEqual(self.users.get_surname(), self.first_user['surname'])

    # Method to set surname
    def test_set_surname(self):
        new_data = 'new_surname'
        self.users.set_surname(new_data)
        self.assertNotEqual(self.users.get_surname(), self.first_user['surname'])
        self.assertEqual(self.users.get_surname(), new_data)

    # Method to get house_number
    def test_get_house_number(self):
        self.assertEqual(self.users.get_house_number(), self.first_user['house_number'])

    # Method to set house_number
    def test_set_house_number(self):
        new_data = 29
        self.users.set_house_number(new_data)
        self.assertNotEqual(self.users.get_house_number(), self.first_user['house_number'])
        self.assertEqual(self.users.get_house_number(), new_data)

    # Method to get street_name
    def test_get_street_name(self):
        self.assertEqual(self.users.get_street_name(), self.first_user['street_name'])

    # Method to set street_name
    def test_set_street_name(self):
        new_data = 'new_street_name'
        self.users.set_street_name(new_data)
        self.assertNotEqual(self.users.get_street_name(), self.first_user['street_name'])
        self.assertEqual(self.users.get_street_name(), new_data)

    # Method to get postcode
    def test_get_postcode(self):
        self.assertEqual(self.users.get_postcode(), self.first_user['postcode'])

    # Method to set postcode
    def test_set_postcode(self):
        new_data = 26353
        self.users.set_postcode(new_data)
        self.assertNotEqual(self.users.get_postcode(), self.first_user['postcode'])
        self.assertEqual(self.users.get_postcode(), new_data)

    # Method to get email_address
    def test_get_email_address(self):
        self.assertEqual(self.users.get_email_address(), self.first_user['email_address'])

    # Method to set email_address
    def test_set_email_address(self):
        new_data = 'test@example.com'
        self.users.set_email_address(new_data)
        self.assertNotEqual(self.users.get_email_address(), self.first_user['email_address'])
        self.assertEqual(self.users.get_email_address(), new_data)

    # Method to get date_of_birth
    def test_get_date_of_birth(self):
        self.assertEqual(self.users.get_date_of_birth(), self.first_user['date_of_birth'])

    # Method to sst date_of_birth
    def test_set_date_of_birth(self):
        new_data = '25-09-1867'
        self.users.set_date_of_birth(new_data)
        self.assertNotEqual(self.users.get_date_of_birth(), self.first_user['date_of_birth'])
        self.assertEqual(self.users.get_date_of_birth(), new_data)

    # Method to edit firstname
    def test_edit_firstname(self):
        self.users.edit_firstname('newFirstname')
        self.assertEqual(self.users.get_firstname(), 'newFirstname')

    # Method to edit surname
    def test_edit_surname(self):
        self.users.edit_surname('newSurname')
        self.assertEqual(self.users.get_surname(), 'newSurname')

    # Method to edit email_address
    def test_edit_email_address(self):
        self.users.edit_email_address('new-email@gmx.de')
        self.assertEqual(self.users.get_email_address(), 'new-email@gmx.de')

    # Method to edit dob
    def test_edit_date_of_birth(self):
        self.users.edit_date_of_birth('25-5-65')
        self.assertEqual(self.users.get_date_of_birth(), '25-5-65')

