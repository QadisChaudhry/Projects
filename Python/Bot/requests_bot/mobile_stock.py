import requests, time, os
from mobileKeys import keys


class Bot:
    def __init__(self, **keys):
        self.base = 'https://www.supremenewyork.com'
        self.s = requests.Session()
        self.keys = keys
        self.products_found = []

    def find_product(self, x):
        try:
            mobile_stock = self.s.get(f'{self.base}/mobile_stock.json', headers=headers).json()

            for i in mobile_stock['products_and_categories'][keys[f'product{x}'][2]]:
                if keys[f'product{x}'][0] in i['name']:
                    self.products_found.append(i['id'])

            item_info = self.s.get(f'{self.base}/shop/{self.products_found[0]}.json', headers=headers).json()

            for i in item_info['styles']:
                if keys[f'product{x}'][1] in i['name']:
                    self.products_found.append(i['id'])
                    self.products_found.append(i['sizes'][0]['id'])
                    fail = False
                else:
                    fail = True
            if fail:
                self.products_found.append(item_info['styles'][0]['id'])
                self.products_found.append(item_info['styles'][0]['sizes'][0]['id'])
            return True
        except:
            return False

    def cart(self):
        payload = {
            's': f'{self.products_found[2]}',
            'st': f'{self.products_found[1]}',
            'qty': '1'
        }
        time.sleep(1)
        add_request = self.s.post(f'{self.base}/shop/{self.products_found[0]}/add.json', headers=headers,
                                  data=payload).json()
        self.products_found = []
        print(add_request)

    def checkout(self):
        checkout_data = {
            'order[billing_name]': keys['name'],
            'cerear': 'RMCEAR',
            'order[email]': keys['email'],
            'order[tel]': keys['phone'],
            'order[billing_address]': keys['address'],
            'order[billing_zip]': keys['zip'],
            'order[billing_city]': 'Brooklyn',
            'order[billing_state]': 'NY',
            'order[billing_country]': 'USA',
            'same_as_billing_address': '1',
            'credit_card[type]': 'credit card',
            'riearmxa': keys['card'],
            'credit_card[month]': keys['month'],
            'credit_card[year]': keys['year'],
            'credit_card[meknk]': keys['cvv'],
            'order[terms]': '1'
        }
        time.sleep(1)
        checkout_request = self.s.post(f'{self.base}/checkout.json', headers=headers, data=checkout_data).json()
        print(checkout_request)
        time.sleep(0.5)
        if checkout_request['status'] == 'queued':
            slug = checkout_request['slug']
            while checkout_request['status'] != 'paid':
                status = self.s.get(f'{self.base}/checkout/{slug}/status.json', headers=headers).json()
                print(status['status'])
                time.sleep(1)
                if status['status'] == 'paid':
                    print('Checkout Succeeded')
                if status['status'] == 'failed':
                    print('Checkout Failed')
                    break
        else:
            print('Checkout Failed')


def main():
    products = list(range(1, int(keys['#_of_products']) + 1))
    found_product = False
    max_count = 10
    count = 0
    start1 = time.time()
    while not found_product and count < max_count:
        found_product = bot.find_product(1)
        count += 1
        print(f'{count}: Looking for Product...')
        print(found_product)
        time.sleep(0.2)
    if found_product:
        start2 = time.time()
        for i in products:
            bot.find_product(i)
            bot.cart()
            time.sleep(0.5)
        bot.checkout()
        end2 = time.time()
        print(f'Checkout time: {round(float(end2 - start2), 4)} seconds')
    else:
        os.system('python3 mobile_stock.py')
        exit(0)
    end1 = time.time()
    print(f'Run time: {round(float(end1 - start1), 4)} seconds')


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)'
                      ' CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }
    bot = Bot(**keys)
    main()
