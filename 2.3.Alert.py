from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Click the button
    button = browser.find_element_by_tag_name("button")
    button.click()

    # Accept Confirm
    alert = browser.switch_to.alert
    alert.accept()

    # Fill the form on new page
    x_value = browser.find_element_by_id("input_value")
    x = x_value.text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    # Submit the form
    submit = browser.find_element_by_tag_name("button")
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()