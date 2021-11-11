import uuid

import utilities


class Users:

    def __init__(
        self,
        username,
        firstname,
        surname,
        house_number,
        street_name,
        postcode,
        email_address,
        date_of_birth
    ):
        self.user_id = uuid.uuid4().hex[:6]
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email_address = email_address
        self.date_of_birth = date_of_birth
        self.validator = utilities.InputValidator()

    # Method to get a user id
    def get_user_id(self):
        return self.user_id

    # Method to get username
    def get_username(self):
        return self.username

    # Method to set username
    def set_username(self, username):
        self.set_prop(username, 'username', 'string')

    # Method to get firstname
    def get_firstname(self):
        return self.firstname

    # Method to set firstname
    def set_firstname(self, firstname):
        self.set_prop(firstname, 'firstname', 'string')

    # Method to get surname
    def get_surname(self):
        return self.surname

    # Method to set surname
    def set_surname(self, surname):
        self.set_prop(surname, 'surname', 'string')

    # Method to get house_number
    def get_house_number(self):
        return self.house_number

    # Method to set house_number
    def set_house_number(self, house_number):
        self.set_prop(house_number, 'house_number', 'int')

    # Method to get street_name
    def get_street_name(self):
        return self.street_name

    # Method to set street_name
    def set_street_name(self, street_name):
        self.set_prop(street_name, 'street_name', 'string')

    # Method to get postcode
    def get_postcode(self):
        return self.postcode

    # Method to set postcode
    def set_postcode(self, postcode):
        self.set_prop(postcode, 'postcode', 'int')

    # Method to get email_address
    def get_email_address(self):
        return self.email_address

    # Method to set email_address
    def set_email_address(self, email_address):
        self.set_prop(email_address, 'email_address', 'string')

    # Method to get date_of_birth
    def get_date_of_birth(self):
        return self.date_of_birth

    # Method to set date_of_birth
    def set_date_of_birth(self, date_of_birth):
        self.set_prop(date_of_birth, 'date_of_birth', 'string')

    # Method to edit firstname
    def edit_firstname(self, firstname):
        self.firstname = firstname

    # Method to edit surname
    def edit_surname(self, surname):
        self.surname = surname

    # Method to edit email_address
    def edit_email_address(self, email_address):
        self.email_address = email_address

    # Method to edit date_of_birth
    def edit_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    # Method to edit username
    def edit_username(self, username):
        self.username = username

    # Method to edit house_number
    def edit_house_number(self, house_number):
        self.house_number = house_number

    # Method to edit street_name
    def edit_street_name(self, street_name):
        self.street_name = street_name

    # Method to edit postcode
    def edit_postcode(self, postcode):
        self.postcode = postcode

    '''
    Method sets property for attributes provided. 
    Returns ValueError if type provided does not match expected data type
    '''
    def set_prop(self, data, attribute, data_type):
        try:
            self.validator.validate_data_type(attribute, data_type)
            setattr(self, attribute, data)
        except ValueError as message:
            print(message)

    def __repr__(self):
        return f'"{self.user_id}" "{self.username}" "{self.firstname}" "{self.surname}" "{self.house_number}" ' \
               f'"{self.street_name}" "{self.postcode}" "{self.email_address}" "{self.date_of_birth}"'
