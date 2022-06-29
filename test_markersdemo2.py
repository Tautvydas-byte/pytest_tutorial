import pytest
import sys


@pytest.mark.skip
def test_login():
	print("Login done")


@pytest.mark.skipif(sys.version_info < (3, 10), reason="Python version not supported")
def test_addProduct():
	print("add product")

@pytest.mark.xfail
def test_logout():
	assert False
	print("Logout done")

@pytest.mark.xfail
def test_closeApplication():
	assert True
	print("Close the application")

@pytest.mark.usefixtures
def test_closeApplication():
	assert True
	print("Close the application")
