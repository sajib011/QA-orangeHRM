import pytest

@pytest.fixture()
def test_browser_launch():
    print('Browser Launch Successfully.')


def test_login_tc001(test_browser_launch):
    print('valid Login done.')


def test_login_tc002(test_browser_launch):
    print('invalid login done.')


def test_browser_close():
    print('Browser Closed')
