"""
Data Processor Module

This module provides a DateProcessor class for handling date-related operations.

Methods:
- parse_dateformat(date: str, date_format: str) -> datetime:
    Parses the input date string using the specified format and
    returns a datetime object.

- calculate_year_difference(dt: datetime) -> int:
    Calculates the difference in years between the input date and
    the current date.

Example:
>>> date_processor = DateProcessor()
>>> parsed_date = date_processor.parse_dateformat("2023-01-01", "%Y-%m-%d")
>>> age = date_processor.calculate_year_difference(parsed_date)
>>> print(age)
1
"""
from datetime import datetime

from dateutil.relativedelta import relativedelta


class DateProcessor:
    """
    DateProcessor class for handling date-related operations.

    Methods:
    - parse_dateformat(date: str, date_format: str) -> datetime:
        Parses the input date string using the specified format and returns a datetime object.

    - calculate_year_difference(dt: datetime) -> int:
        Calculates the difference in years between the input date and the current date.

    Example:
    >>> date_processor = DateProcessor()
    >>> parsed_date = date_processor.parse_dateformat("2023-01-01", "%Y-%m-%d")
    >>> age = date_processor.calculate_year_difference(parsed_date)
    >>> print(age)
    1
    """

    @staticmethod
    def parse_dateformat(date: str, date_format: str) -> datetime:
        """
        Parses the input date string using the specified format and returns a datetime object.

        Parameters:
        - date (str): The date string to be parsed.
        - date_format (str): The format of the input date string.

        Returns:
        - datetime: A datetime object representing the parsed date.

        Example:
        >>> date_processor = DateProcessor()
        >>> parsed_date = date_processor.parse_dateformat("2023-01-01", "%Y-%m-%d")
        >>> print(parsed_date)
        2023-01-01 00:00:00
        """
        return datetime.strptime(date, date_format)

    @staticmethod
    def calculate_year_difference(dt: datetime) -> int:
        """
        Calculates the difference in years between the input date and the current date.

        Parameters:
        - dt (datetime): The date for which the age difference is calculated.

        Returns:
        - int: The difference in years.

        Example:
        >>> date_processor = DateProcessor()
        >>> age = date_processor.calculate_year_difference(datetime(1990, 5, 15))
        >>> print(age)
        32
        """
        return relativedelta(datetime.now(), dt).years
