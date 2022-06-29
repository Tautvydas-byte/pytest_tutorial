"""
Precondition
	Setup, Connection, API

	Test

	Test

	Assertion

	Postcon
		clean, close, close
"""
# https://docs.pytest.org/en/6.2.x/fixture.html
import pytest
from selenium import webdriver

driver=None

@pytest.fixture  # let not to write the same thing again and again
def setup():
	print("Start Browser")
	global driver
	PATH = "C:/Users/tautv/Downloads/Programos/chromedriver_win32/chromedriver.exe"
	driver = webdriver.Chrome(PATH)
	driver.maximize_window()
	yield
	driver.quit()
	print("Close Browser")


def test_1(setup):
	# print("Start Browser")
	driver.get("https://www.youtube.com")
	print("Test 1 executed")
	# print("Close Browser")

def test_2(setup):
	# print("Start Browser")
	driver.get("http://www.google.com")
	print("Test 2 executed")
	# print("Close Browser")

def test_3(setup):
	# print("Start Browser")
	driver.get("http://www.gmail.com")
	print("Test 3 executed")
# print("Close Browser")

# pytest test_fixtures.py -s <- -s for show below field

#https://pypi.org/project/pytest-xdist/ <- plugin extends pytest with new test execution modes, the most used being
# distributing tests across multiple CPUs to speed up test execution:
#pytest test_fixtures.py -n 3
