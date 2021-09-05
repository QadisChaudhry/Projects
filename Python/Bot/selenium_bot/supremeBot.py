import requests, time, os
from selenium import webdriver
from bs4 import BeautifulSoup
from supremeBotKeys import keys


class Bot:
    def __init__(self, **keys):
        self.base = 'https://www.supremenewyork.com'
        self.shop_ext = '/shop'
        self.checkout_ext = '/checkout'
        self.keys = keys
        self.driver = webdriver.Chrome()

    def find_product(self, x):
        try:
            r = requests.get(self.keys['url_{}'.format(self.keys['product{}'.format(x)][2])]).text
            soup = BeautifulSoup(r, 'lxml')

            temp_tuple = []
            temp_link = []

            for link in soup.find_all('a', href=True):
                temp_tuple.append((link['href'], link.text))

            for i in temp_tuple:
                if i[1] == self.keys['product{}'.format(x)][0] or i[1] == self.keys['product{}'.format(x)][0] + " " \
                        or i[1] == self.keys['product{}'.format(x)][1]:
                    temp_link.append(i[0])

            self.final_link = list(set([x for x in temp_link if temp_link.count(x) == 2]))[0]
            return True
        except:
            return False

    def cart(self):
        self.driver.get('{}{}'.format(self.base, self.final_link))
        self.driver.find_element_by_name('commit').click()

    def checkout(self):
        time.sleep(0.8)
        while self.driver.current_url != self.base + self.checkout_ext:
            self.driver.get('{}{}'.format(self.base, self.checkout_ext))

        self.driver.find_element_by_id('order_billing_name').send_keys(self.keys['name'])
        self.driver.find_element_by_id('order_email').send_keys(self.keys['email'])
        self.driver.find_element_by_id('order_tel').send_keys(self.keys['phone'])
        self.driver.find_element_by_id('bo').send_keys(self.keys['address'])
        self.driver.find_element_by_id('order_billing_zip').send_keys(self.keys['zip'])
        self.driver.find_element_by_id('rnsnckrn').send_keys(self.keys['card'])
        self.driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[4]').click()
        self.driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[2]').click()
        self.driver.find_element_by_id('orcer').send_keys(self.keys['cvv'])
        self.driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()
        self.driver.find_element_by_name('commit').click()

    def main(self):
        products = list(range(1, int(keys['#_of_products']) + 1))
        found_product = False
        max_count = 20
        count = 1
        while not found_product and count < max_count:
            found_product = bot.find_product(1)
            count += 1
        if found_product:
            start = time.time()
            for i in products:
                bot.find_product(i)
                bot.cart()
            bot.checkout()
            end = time.time()
            print(end - start)
        else:
            self.driver.quit()
            os.system('python3 supremeBot.py')


if __name__ == '__main__':
    bot = Bot(**keys)
    bot.main()
