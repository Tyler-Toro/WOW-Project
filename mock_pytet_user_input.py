import pytest
import mock
import module
import builtins
def user_prompt():
    ans = input('Enter a number: ')
    try:
        str(ans)
    except:
        import sys
        sys.exit('NaN')
    return 'Your number is {}'.format(ans)

def test_user_prompt_ok():
    with mock.patch.object(builtins, 'input', lambda _: '19'):
        assert user_prompt() == 'Your number is 19'

def test_user_prompt_ok2():
    with mock.patch.object(builtins, 'input', lambda _: 'hi there'):
        assert user_prompt() == 'Your number is hi there'