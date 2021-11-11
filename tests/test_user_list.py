import unittest

from Model.Books import Books
from Model.user_list import UserList
from Model.users import Users


class TestUserList(unittest.TestCase):
    # initial setup to test books class
    def setUp(self) -> None:
        user_list = UserList()
        first_user_list = [
            {
                'username': 'user_one',
                'firstname': 'UserOne',
                'surname': 'One',
                'street_name': 'Yaba',
                'house_number': 25,
                'postcode': 2554,
                'email_address': 'userone@gmx.de',
                'date_of_birth': '02-05-97',
            },
            {
                'username': 'user_two',
                'firstname': 'UserTwo',
                'surname': 'Two',
                'street_name': 'Hamburg',
                'house_number': 5,
                'postcode': 22897,
                'email_address': 'usertwo@gmx.de',
                'date_of_birth': '12-02-69',
            },
        ]
        for user in first_user_list:
            user_list.user_list.append(Users(**user))
        self.user_list = user_list

    # Test method to add new user to user list
    def test_add(self):
        self.user_list.add(
            Users(**{
                'username': 'user_three',
                'firstname': 'UserThree',
                'surname': 'Three',
                'street_name': 'Hamburg',
                'house_number': 55,
                'postcode': 10234,
                'email_address': 'userthree@gmx.de',
                'date_of_birth': '21-12-99',
            })
        )
        self.assertEqual(3, len(self.user_list.user_list))

    # Test method to remove user from user list
    def test_remove(self):
        self.user_list.remove(self.user_list.user_list[0])
        self.assertEqual(1, len(self.user_list.user_list))

    # Test method to get user from user list
    def test_get_user_by_username(self):
        user = self.user_list.get_user_by_username('user_one')
        self.assertEqual(self.user_list.user_list[0].username, user.username)
