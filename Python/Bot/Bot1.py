from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Keys1 import keys
import os
import time


def cart():
	wait.until(ec.element_to_be_clickable((By.NAME, 'commit')))
	driver.find_element_by_name('commit').click()


def checkout():
	wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="cart"]/a[2]')))
	driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

	driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys['name'])
	driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys['email'])
	driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys['phone'])
	driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys['address'])
	driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip'])
	driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(keys['card'])
	driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[4]').click()
	driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[2]').click()
	driver.find_element_by_id('orcer').send_keys(keys['cvv'])
	driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
	driver.find_element_by_xpath('//*[@id="pay"]/input').click()


def get_product(x):
	driver.get(keys['url_{}'.format(keys['product{}'.format(x)][1])])
	driver.find_element_by_partial_link_text(keys['product{}'.format(x)][0]).click()
	cart()
	time.sleep(0.1)


def main():
	try:
		products = list(range(1, int(keys['#_of_products']) + 1))
		for i in products:
			get_product(i)
		checkout()
	except KeyboardInterrupt:
		driver.quit()
		os.system('python3 Bot1.py')


if __name__ == '__main__':
	driver = webdriver.Chrome()
	wait = WebDriverWait(driver, 5)
	start = time.time()
	main()
	end = time.time()
	print(end - start)
