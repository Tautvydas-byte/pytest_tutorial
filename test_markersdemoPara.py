import pytest
import sys


# https://docs.pytest.org/en/6.2.x/parametrize.html
@pytest.mark.parametrize("username,password", [("Selenium", "WebDriver"), ("Python", "Pytest"), ("Vytautas", "Kvk"),("API", "Web")])
def test_login(username, password):
	print(username)
	print(password)
