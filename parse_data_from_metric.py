import json
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Скрипт использовался для сбора данных из Яндекс.Метрики

email = "login"
password = "pass"
result = []

driver = webdriver.Chrome()
driver.get("https://metrika.yandex.ru")
elem = driver.find_element_by_css_selector(".button2")
elem.click()
elem_mail = driver.find_element_by_id("passp-field-login")
elem_btn_login = driver.find_element_by_css_selector(".Button2_type_submit")
elem_mail.send_keys(email)
elem_btn_login.click()
try:
    elem_password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passp-field-passwd"))
    )
    elem_password.send_keys(password)
    elem_btn_login = driver.find_element_by_css_selector(".Button2_type_submit")
    elem_btn_login.click()
except Exception as e:
    print(e)
time.sleep(5)
driver.get("https://metrika.yandex.ru/goals?id=80976547")
try:
    with open("data.json", "r", encoding="utf-8") as f:
        json_data = f.read()
        data = json.loads(json_data)
    for el in data:
        print(el)
        btn_add = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div[3]/div/div/form/div[3]/div[2]/div[3]"
                                                "/div/div[2]/div[2]/button")
        btn_add.click()

        time.sleep(3)
        el_title = driver.find_element(By.CSS_SELECTOR, ".modal__content .input__control")
        el_title.send_keys(el["name"])
        radio = driver.find_elements(By.CSS_SELECTOR, "input.radio-button__control[type='radio']")
        for btn in radio:
            if btn.get_attribute("value") == "action":
                btn.click()
        el_value = driver.find_element(By.CSS_SELECTOR, ".counter-edit-goal__tab-action .input__control")
        el_value.send_keys(el["value"])
        save = driver.find_element(By.CSS_SELECTOR, ".i-confirm-popup__buttons .i-confirm-popup__button")
        save.click()

except Exception as e:
    print(e)
else:
    print("The script finished its work.")
assert "No results found." not in driver.page_source
driver.close()
