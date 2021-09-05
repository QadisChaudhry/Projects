from selenium import webdriver
from Keys2 import keys
from selenium.common.exceptions import InvalidSelectorException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import pyautogui as pg
import os


def cart():
	wait.until(ec.element_to_be_clickable((By.NAME, 'add')))
	driver.find_element_by_name('add').click()


def checkout():
	wait.until(ec.element_to_be_clickable((By.NAME, 'checkout')))
	driver.find_element_by_name('checkout').click()

	wait.until(ec.visibility_of_element_located((By.ID, 'checkout_email')))
	driver.find_element_by_id('checkout_email').send_keys(keys['email'])
	time.sleep(0.2)

	driver.find_element_by_id('checkout_shipping_address_first_name').send_keys(keys['firstName'])
	driver.find_element_by_id('checkout_shipping_address_last_name').send_keys(keys['lastName'])
	driver.find_element_by_id('checkout_shipping_address_address1').send_keys(keys['address'])
	driver.find_element_by_id('checkout_shipping_address_city').send_keys(keys['city'])
	driver.find_element_by_xpath('//*[@id="checkout_shipping_address_province"]/option[37]').click()
	driver.find_element_by_id('checkout_shipping_address_zip').send_keys(keys['zip'])
	for i in keys['phone']:
		driver.find_element_by_id('checkout_shipping_address_phone').send_keys(i)
		time.sleep(0.01)

	driver.find_element_by_xpath('//*[@id="continue_button"]').click()
	wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="continue_button"]')))
	driver.find_element_by_xpath('//*[@id="continue_button"]').click()

	wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="main-header"]')))
	pg.moveTo(320, 635)
	pg.click()
	pg.typewrite(keys['card'])
	pg.press('tab')
	pg.typewrite(keys['firstName'] + ' ' + keys['lastName'])
	pg.press('tab')
	pg.typewrite(keys['expDate'])
	pg.press('tab')
	pg.typewrite(keys['cvv'])

	# driver.find_element_by_xpath('//*[@id="continue_button"]').click()


def size(x):
	if x == '':
		pass
	else:
		try:
			driver.find_element_by_css_selector('div.swatch-element.{}'.format(x)).click()
		except InvalidSelectorException:
			try:
				driver.find_element_by_xpath('//*[@for="swatch-0-{}"]'.format(x)).click()
			except NoSuchElementException:
				pass


def get_product(n):
	driver.get(keys['url' + str(n)])
	size(keys['size' + str(n)])
	cart()


if __name__ == '__main__':
	driver = webdriver.Chrome()
	wait = WebDriverWait(driver, 5)
	try:
		get_product(1)
		get_product(2)
		# get_product(3)
		checkout()
	except KeyboardInterrupt:
		driver.quit()
		# os.system('python3 Bot2.py')
