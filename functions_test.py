from ETS_functions import create_string_from_int_list
import pytest
def test_create_string_from_int_list():
  expected = "1234"
  actual = create_string_from_int_list([1, 2, 3, 4])
  assert actual == expected