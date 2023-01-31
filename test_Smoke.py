import datetime

# ПОЗИТИВНЫЙ ТЕСТ

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(options=options)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# Объявляем переменные логинов будет несколько , а пароль будет одинаковый для всех
login_standard_user = "standard_user"
password_all = "secret_sauce"

# Вводим логин
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input login")

# Вводим пароль
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("Input Password")

# Нажимаем на кнопку LOGIN
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click login button")

"""INFO PRODUCT 1"""
# НАХОДИМ НАЗВАНИЕ ТОВАРА
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

# НАХОДИМ ЦЕНУ ТОВАРА
price_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

# НАЖИМАЕМ КНОПКУ ДОБАВИТЬ ТОВАР В КОРЗИНУ
select_product_1 = driver.find_element(By.XPATH, "//Button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print("Товар добавлен в корзину")

# ПЕРЕХОД В КОРЗИНУ
shopping_cart_badge = driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']")
shopping_cart_badge.click()
print("Enter cart")

"""INFO CART"""
# Сравниваем название товара в корзине с названием на странице товара
cart_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("ОК")
# Сравниваем цену в корзине с ценой на странице товара
price_cart_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print("OK")
# Наимаем кнопку checkout
checkout_button = driver.find_element(By.XPATH, "//Button[@id='checkout']")
checkout_button.click()
print("Click checkout")

"""SELECT USER INFO"""
# Вводим имя
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys("Ivan")
print("input first name")
# Вводим фамилию
last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys("Ivanov")
print("input last name")
# Вводим почтовый код
zip_postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip_postal_code.send_keys("1234")
print("input zip/postal cod")
# Нажимаем кнопку продолжить
continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
continue_button.click()
print("Click continue")

""" INFO FINISH PRODUCT"""
# Сравниваем наименование с начальным
finish_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("ОК")
# Сравниваем цену с начальной
price_finish_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("OK")
#
summary_price = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
value_summary_price = summary_price.text
print(value_summary_price)

item_total = "Item total: " + value_finish_price_product_1
assert value_summary_price == item_total
print("total price good")

finish = driver.find_element(By.XPATH, "//button[@id='finish']")
finish.click()
print("покупка совершена")

back = driver.find_element(By.XPATH, "//button[@id='back-to-products']")
back.click()