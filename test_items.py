import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_presence_add_cart_button(browser):
    browser.get(link)
    submit_button = browser.find_elements_by_class_name('btn-add-to-basket')
    time.sleep(30)
    assert submit_button != [], "There is no add to cart button"
