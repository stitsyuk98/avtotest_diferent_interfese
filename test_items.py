import pytest
from selenium import webdriver
import conftest
from selenium.webdriver.chrome.options import Options


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.btn-add-to-basket")