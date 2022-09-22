from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_btn_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    message = browser.find_element(By.CLASS_NAME, "btn-add-to-basket").text
    assert len(message) != 0, "The product page on the website does not contain an add to cart button"
