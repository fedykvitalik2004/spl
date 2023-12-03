"""
JSON Processor Module

This module provides functions for working with JSON data. It includes functions
for flattening nested JSON structures
and displaying flattened JSON data with colored output.

Usage:
1. Import the module: `import src.shared.json_processor as json_processor`
2. Use the provided functions to process JSON data.

Note: Ensure the required libraries (`colorama`) are installed before using this module.
You can install it using: `pip install colorama`

Example:
```python
import src.shared.json_processor as json_processor

# Flatten a nested JSON structure
json_data = {'name': 'John', 'address': {'city': 'New York', 'zip': '10001'}}
flattened_data = json_processor.flatten_json(json_data)
print(flattened_data)
# {'name': 'John', 'address_city': 'New York', 'address_zip': '10001'}

# Display flattened JSON data with colored output
json_processor.display_flattened_json([json_data], color_position=2)
"""
from colorama import Fore
from src.shared import color_processor


def flatten_json(json_data: dict, parent_key: str = '', delimiter='_'):
    """
      Flattens a nested JSON structure and returns a flattened dictionary.

      Parameters:
      - json_data (dict): The nested JSON structure to be flattened.
      - parent_key (str): The parent key used for constructing flattened
      keys (default is an empty string).
      - delimiter (str): The delimiter used between keys in the
      flattened structure (default is '_').

      Returns:
      - dict: A flattened dictionary.

      Example:
      >>> import src.shared.json_processor as json_processor
      >>> json_data = {'name': 'John', 'address': {'city': 'New York', 'zip': '10001'}}
      >>> flattened_data = json_processor.flatten_json(json_data)
      >>> print(flattened_data)
      {'name': 'John', 'address_city': 'New York', 'address_zip': '10001'}
      """
    if (not isinstance(json_data, dict) and not isinstance(parent_key, str)
            and not isinstance(delimiter, str)):
        raise ValueError("Wrong data types!")
    flat_data = {}

    for key, value in json_data.items():
        new_key = parent_key + delimiter + key if parent_key else key

        if isinstance(value, dict):
            flat_data.update(flatten_json(value, new_key, delimiter))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                flat_data.update(flatten_json({str(i): item}, new_key, delimiter))
        else:
            flat_data[new_key] = value

    return flat_data


def display_flattened_json(jsons, color_position: int = 4):
    """
    Displays flattened JSON data with colored output.

    Parameters:
    - jsons: The JSON data to be displayed (can be a dictionary or a list of dictionaries).
    - color_position (int): The position of the color in the
    color_processor.colors dictionary (default is 4).

    Raises:
    - ValueError: If data types or color position are incorrect.

    Example:
    >>> import src.shared.json_processor as json_processor
    >>> json_data = {'name': 'John', 'address': {'city': 'New York', 'zip': '10001'}}
    >>> json_processor.display_flattened_json([json_data], color_position=2)
    name: John
    address_city: New York
    address_zip: 10001
    """
    if ((not isinstance(jsons, dict) or not isinstance(jsons, list))
            and not isinstance(color_position, int)):
        raise ValueError("Wrong data types!")
    elif color_position < 0 or color_position > len(color_processor.colors):
        raise ValueError("Wrong color position!")
    if isinstance(jsons, list):
        for counter, json_data in enumerate(jsons):
            flat_json = flatten_json(json_data)
            for key, value in flat_json.items():
                print(Fore.__getattribute__(
                    color_processor.colors[color_position]) + f'{key}:' + Fore.RESET + f' {value}')
    elif isinstance(jsons, dict):
        flat_json = flatten_json(jsons)
        for key, value in flat_json.items():
            print(Fore.__getattribute__(color_processor.colors[color_position]) +
                  f'{key}:' + Fore.RESET + f' {value}')
