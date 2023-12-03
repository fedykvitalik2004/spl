"""
User Entity Module

This module defines the `User` class representing a user with various attributes.

Attributes:
- index (int): The index of the user.
- user_id (str): The unique identifier for the user.
- first_name (str): The first name of the user.
- last_name (str): The last name of the user.
- sex (str): The gender of the user.
- email (str): The email address of the user.
- phone (str): The phone number of the user.
- date_of_birth (datetime.date): The date of birth of the user, parsed from
the specified format ("%Y-%m-%d").
- job_title (str): The job title of the user.

Methods:
- __init__(self, data): Initializes a User object with the given data.
- __str__(self): Returns a string representation of the User object.

Example:
```python
data = [1, '12345', 'John', 'Doe', 'Male', 'john.doe@example.com',
        '123-456-7890', '1990-01-01', 'Engineer']
user = User(data)
print(user)
# Output: 1 12345 John Doe Male john.doe@example.com 123-456-7890 1990-01-01 Engineer
"""
from src.shared.data_processor import DateProcessor


class User:
    """
    Represents a user with various attributes.

    Attributes:
    - index (int): The index of the user.
    - user_id (str): The unique identifier for the user.
    - first_name (str): The first name of the user.
    - last_name (str): The last name of the user.
    - sex (str): The gender of the user.
    - email (str): The email address of the user.
    - phone (str): The phone number of the user.
    - date_of_birth (datetime.date): The date of birth of
    the user, parsed from the specified format ("%Y-%m-%d").
    - job_title (str): The job title of the user.

    Methods:
    - __init__(self, data): Initializes a User object with the given data.
    - __str__(self): Returns a string representation of the User object.

    Example:
    >>> data = [1, '12345', 'John', 'Doe', 'Male', 'john.doe@example.com',
    '123-456-7890', '1990-01-01', 'Engineer']
    >>> user = User(data)
    >>> print(user)
    1 12345 John Doe Male john.doe@example.com 123-456-7890 1990-01-01 Engineer
    """

    def __init__(self, data):
        """
        Initialize User object with the given data.

        Parameters:
        - data (list): A list containing values for each attribute in the specified order.
        """
        self.index = data[0]
        self.user_id = data[1]
        self.first_name = data[2]
        self.last_name = data[3]
        self.sex = data[4]
        self.email = data[5]
        self.phone = data[6]
        # parse the eighth value of the data list as a date in the format "%Y-%m-%d"
        # and assign it to the date_of_birth attribute
        self.date_of_birth = DateProcessor.parse_dateformat(data[7], "%Y-%m-%d").date()
        self.job_title = data[8]

    def __str__(self):
        """
        Return a string representation of the User object.

        Returns:
        - str: A string containing user information.
        """
        return (f"{self.index} {self.user_id} {self.first_name} {self.last_name} {self.sex} "
                f"{self.email} {self.phone} {self.date_of_birth} {self.job_title}")
