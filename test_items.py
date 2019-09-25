from selenium import webdriver
import time
import pytest


class TestStore(object):
    def test_addtocart_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        buttons = browser.find_elements_by_class_name("btn-add-to-basket")
        numberofbuttons = len(buttons)
        assert numberofbuttons < 2, f"Unexpected buttons with the same class 'btn-add-to-basket'"
        assert numberofbuttons == 1, f"No buttons found with class 'btn-add-to-basket'"
