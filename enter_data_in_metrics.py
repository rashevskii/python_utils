from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Скрипт использовался для автоматизации введения заранее собранных данных в Яндекс.Метрику

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
driver.get("https://metrika.yandex.ru/goals?id=79510717")
try:
    x = 0
    y = 600
    elems_edit = driver.find_elements(By.CLASS_NAME, "counter-edit-table-row__edit-goal")
    for el in elems_edit:
        el.click()
        time.sleep(0.5)
        el_goal = driver.find_element(By.CSS_SELECTOR, ".modal__cell .counter-edit-goal__body "
                                                       ".radio-button__radio_checked_yes .radio-button__text")
        if el_goal.get_attribute("textContent") == "JavaScript-событие ":
            el_title = driver.find_element(By.CSS_SELECTOR, ".modal__content .input__control")
            el_value = driver.find_element(By.CSS_SELECTOR, ".counter-edit-goal__tab-action .input__control")
            result.append({"name": el_title.get_attribute("value"), "value": el_value.get_attribute("value")})
        el_close = driver.find_element(By.XPATH, "/html/body/div[14]/div/div/div/div[2]/button")
        el_close.click()
        driver.execute_script(f"window.scrollTo({x}, {y})")
        x = y
        y += 100
    with open("data.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(result))

except Exception as e:
    print(e)
assert "No results found." not in driver.page_source
driver.close()
