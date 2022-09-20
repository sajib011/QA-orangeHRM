import pytest


def test_login_valid():
    print('Login Success,Test Passed')


def test_login_invalid():
    print('Login Failed,Test passed')


def test_forcefully_failed():
    assert False
