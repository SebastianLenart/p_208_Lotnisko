import requests
import unittest
from unittest.mock import Mock



my_mock = Mock()
my_mock.some_method.return_value = 42
my_mock.some_attribute = "Hello, world!"
my_mock.some_method.side_effect = ValueError("Something went wrong")


