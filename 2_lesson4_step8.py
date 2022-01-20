from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Дожидаемся когда цена станет равной 100
    myPrice = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )

    submit = browser.find_element_by_css_selector(".btn.btn-primary").click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    submit = browser.find_element_by_css_selector("#solve.btn.btn-primary")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
