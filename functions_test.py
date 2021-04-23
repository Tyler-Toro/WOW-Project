import pytest
import sys
import time
import builtins
import os
import mock
from ETS_functions import header


# Function tests rooftop puzzle 

def create_string_from_int_list(intList):
  return "".join([str(x) for x in intList])


def test_create_string_from_int_list():
  expected = "1234"
  actual = create_string_from_int_list([1, 2, 3, 4])
  assert actual == expected

# Imported from ETS_functions()
'''

def header():
    fast_text("  \t\t   .... ............... ..........................\n\
  \t\t   .. ......................... .......... .......\n\
  \t\t   ...... ..... ......... ........................\n\
  \t\t   .........  Escaping Toro Sanctum...... ........\n\
  \t\t   ........ ............... ............... ......\n\
  \t\t   :::::::::::::::::::::::::::::::::::::::::::::::\n\
  \t\t   :::::::::::::::::::::::::::::::::::::::::::::::\n\n\n")

'''

def fast_text(text, delay = 0):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0)
    time.sleep(0)



def test_header(capsys):
    header()
    captured = capsys.readouterr()
    assert captured.out == ("  \t\t   .... ............... ..........................\n\
  \t\t   .. ......................... .......... .......\n\
  \t\t   ...... ..... ......... ........................\n\
  \t\t   .........  Escaping Toro Sanctum...... ........\n\
  \t\t   ........ ............... ............... ......\n\
  \t\t   :::::::::::::::::::::::::::::::::::::::::::::::\n\
  \t\t   :::::::::::::::::::::::::::::::::::::::::::::::\n\n\n")




# Function user_prompt tests: 1) user_name input in Player Class 2) user_name populated into starting_question()

def user_prompt():
    user_name = input("What is your name, Team Leader?:\n")
    try:
        str(user_name)
    except:
        import sys
        sys.exit('NaN')
    return f"{user_name}, would you like to Start? (Y/N):\n"



def test_user_prompt_ok():
    with mock.patch.object(builtins, 'input', lambda _: 'Tyler'):
        assert user_prompt() == "Tyler, would you like to Start? (Y/N):\n"

