import pytest, time
from selenium import webdriver
import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestFindButton():
    def test_find_button(self, browser):
        browser.get(link)
        btn = browser.find_elements_by_css_selector("button.btn-add-to-basket")
        assert len(btn) == 1, 'i haven"t button'