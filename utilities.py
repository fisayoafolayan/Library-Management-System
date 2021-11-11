"""
helper class that serves as input validator
"""


class InputValidator:
    def validate_data_type(self, data_input, data_type):
        if isinstance(data_input, type(data_type)) and data_input != '':
            return True
        else:
            return False

    """
    An helper function to count to provide a count of the header
    Example, 5 returns [1,2,3,4,5]
    """
    def get_column_count(self, number):
        column_count = list(range(number, 0, -1))
        return column_count[::-1]
