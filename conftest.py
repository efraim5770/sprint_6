import pytest
from selenium import webdriver
from urls import URLs


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(URLs.scooter_adress)
    yield driver
    driver.quit()