import requests
import time
import os
import json
from termcolor import colored


class Menu:
    def __init__(self):
        self.profile = json.load(open("profile.json"))
        self.product = json.load(open("products.json"))

    def start(self):
        print(colored("Main Menu", "yellow"))
        print("1: Product")
        print("2: Profile")
        print("3: Run\n")

        selection = input("> ")

        if selection == "1":
            menu.product_menu()
        elif selection == "2":
            menu.profile_menu()
        elif selection == "3":
            confirmation = input("\nrun all? [y/n] ")
            if confirmation == "y" or confirmation == "":
                for i in range(20):
                    print(".")
                    time.sleep(0.05)
                bot.main()
            elif confirmation == "n":
                print(colored("returning to menu...\n", "red"))
                menu.start()
            else:
                print(colored("returning to menu...\n", "red"))
                menu.start()
        elif selection == "q":
            exit(0)
        else:
            print(colored("\nEnter a Valid Selection\n", "red"))
            menu.start()

    def product_menu(self):
        print(colored("\nProducts", "yellow"))
        print("0: Back")
        print("1: Enter Products")
        print("2: View Products\n")

        selection = input("> ")

        if selection == "0":
            print()
            menu.start()
        elif selection == "1":
            menu.enter_product()
            menu.product_menu()
        elif selection == "2":
            self.product = json.load(open("products.json"))
            menu.view_product()
            menu.product_menu()
        else:
            print(colored("\nEnter a Valid Selection", "red"))
            menu.product_menu()

    def profile_menu(self):
        print(colored("\nProfile", "yellow"))
        print("0: Back")
        print("1: Edit Profile")
        print("2: View Profile\n")

        selection = input("> ")

        if selection == "0":
            print()
            menu.start()
        elif selection == "1":
            menu.edit_profile()
            menu.start()
        elif selection == "2":
            self.profile = json.load(open("profile.json"))
            menu.view_profile()
            menu.start()
        else:
            print(colored("\nEnter a Valid Selection", "red"))
            menu.profile_menu()

    def enter_product(self):
        number_of_products = input("\nNumber of Products (1-3): ")

        if number_of_products == "1":
            products = {"number_of_products": number_of_products,
                        "product 1": input("Product Name: "),
                        "category 1": input("Enter Category: "),
                        "color 1": input("Enter Product Color: "),
                        "delay": "1.5"}
        elif number_of_products == "2":
            products = {"number_of_products": number_of_products,
                        "product 1": input("Product Name: "),
                        "category 1": input("Enter Category: "),
                        "color 1": input("Enter Product Color: "),
                        "product 2": input("Product Name: "),
                        "category 2": input("Enter Category: "),
                        "color 2": input("Enter Product Color: "),
                        "delay": "0.8"}
        elif number_of_products == "3":
            products = {"number_of_products": number_of_products,
                        "product 1": input("Product Name: "),
                        "category 1": input("Enter Category: "),
                        "color 1": input("Enter Product Color: "),
                        "product 2": input("Product Name: "),
                        "category 2": input("Enter Category: "),
                        "color 2": input("Enter Product Color: "),
                        "product 3": input("Product Name: "),
                        "category 3": input("Enter Category: "),
                        "color 3": input("Enter Product Color: "),
                        "delay": "0.5"}
        else:
            print(colored("\nEnter Number From 1-3", "red"))
            menu.enter_product()

        with open("products.json", "w") as f:
            json.dump(products, f)
        print()

        menu.start()

    def view_product(self):
        print()
        for key in self.product:
            if key != "number_of_products" and key != "delay":
                capitalized_key = " ".join(k.capitalize() for k in key.split("_"))
                key_value = self.product[key]
                print("{}: {}".format(colored(capitalized_key, "magenta"), key_value))
        print()

        menu.start()

    def edit_profile(self):
        print()
        profile = {"name": input("Cardholder's Name: "),
                   "email": input("Email: "),
                   "phone": input("Phone: "),
                   "address": input("Address: "),
                   "zip": input("Zipcode: "),
                   "card": input("Card Number: "),
                   "month": input("Card Expiration Month: "),
                   "year": input("Card Expiration Year: "),
                   "cvv": input("Card CVV: ")}

        with open("profile.json", "w") as f:
            json.dump(profile, f)
        print()

        menu.start()

    def view_profile(self):
        print()
        for key in self.profile:
            capitalized_key = " ".join(k.capitalize() for k in key.split("_"))
            key_value = self.profile[key]
            print("{}: {}".format(colored(capitalized_key, "magenta"), key_value))
        print()

        menu.start()


class Bot:
    def __init__(self):
        self.base = "https://www.supremenewyork.com"
        self.s = requests.Session()
        self.products_found = []
        self.profile = json.load(open("profile.json"))
        self.product = json.load(open("products.json"))
        self.start = time.time()

    def find_product(self, x):
        try:
            mobile_stock = self.s.get(f"{self.base}/mobile_stock.json", headers=headers).json()

            for i in mobile_stock["products_and_categories"][self.product[f"category {x}"]]:
                if self.product[f"product {x}"] in i["name"]:
                    self.products_found.append(i["id"])

            item_info = self.s.get(f"{self.base}/shop/{self.products_found[0]}.json", headers=headers).json()

            for i in item_info["styles"]:
                if self.product[f"color {x}"] in i["name"]:
                    self.products_found.append(i["id"])
                    self.products_found.append(i["sizes"][0]["id"])
                    fail = False
                else:
                    fail = True
            if fail:
                self.products_found.append(item_info["styles"][0]["id"])
                self.products_found.append(item_info["styles"][0]["sizes"][0]["id"])
            self.products_found = self.products_found[0:3]
            return True
        except:
            return False

    def cart(self, delay):
        payload = {
            "s": f"{self.products_found[2]}",
            "st": f"{self.products_found[1]}",
            "qty": "1"
        }
        time.sleep(delay)
        add_request = self.s.post(f"{self.base}/shop/{self.products_found[0]}/add.json", headers=headers,
                                  data=payload).json()
        # print(add_request)
        self.products_found = []
        return add_request["success"]

    def checkout(self, delay):
        checkout_data = {
            "order[billing_name]": self.profile["name"],
            "cerear": "RMCEAR",
            "order[email]": self.profile["email"],
            "order[tel]": self.profile["phone"],
            "order[billing_address]": self.profile["address"],
            "order[billing_zip]": self.profile["zip"],
            "order[billing_city]": "Brooklyn",
            "order[billing_state]": "NY",
            "order[billing_country]": "USA",
            "same_as_billing_address": "1",
            "credit_card[type]": "credit card",
            "riearmxa": self.profile["card"],
            "credit_card[month]": self.profile["month"],
            "credit_card[year]": self.profile["year"],
            "credit_card[meknk]": self.profile["cvv"],
            "order[terms]": "1"
        }
        print(colored("Checkout", attrs=["bold"]))
        print(colored("  Checking Out...", "white"))
        time.sleep(delay)
        checkout_request = self.s.post(f"{self.base}/checkout.json", headers=headers, data=checkout_data).json()
        # print(checkout_request)
        time.sleep(0.5)
        end = time.time()
        if checkout_request["status"] == "queued":
            slug = checkout_request["slug"]
            print(colored("  Status: ", "white") + colored("Queued", "yellow"))
            while checkout_request["status"] != "paid":
                status = self.s.get(f"{self.base}/checkout/{slug}/status.json", headers=headers).json()
                time.sleep(1)
                if status["status"] == "paid":
                    print(colored("  Status: ", "white") + colored("Paid", "green"))
                    print(colored("  Checkout Succeeded", 'green'))
                    break
                if status["status"] == "failed":
                    print(colored("  Status: ", "white") + colored("Failed", "red"))
                    print(colored("  Checkout Failed", "red"))
                    break
        else:
            print(colored("  Checkout Failed", "red"))
        print(colored(f"  Bot run time: {round(end - self.start, 4)} seconds\n", "cyan"))

    def main(self):
        self.profile = json.load(open("profile.json"))
        self.product = json.load(open("products.json"))
        products = list(range(1, int(self.product["number_of_products"]) + 1))
        delay = float(self.product["delay"])
        found_product = False
        max_count = 10
        count = 0
        if not found_product:
            print("---------------------------")
            print(colored("Looking for Product...", attrs=["bold"]))
            while not found_product and count < max_count:
                found_product = bot.find_product(1)
                count += 1
                time.sleep(0.2)
            if found_product:
                print(colored("Products Found!", "green"))
                self.start = time.time()
                time.sleep(0.2)
                print(colored("Cart", attrs=["bold"]))
                count = 1
                for i in products:
                    bot.find_product(i)
                    print(colored(f"  ({count}) Adding to Cart...", "white"))
                    success = bot.cart(delay)
                    if not success:
                        print(colored("      Waiting for restock...", "red"))
                        while not success:
                            self.product = json.load(open("products.json"))
                            time.sleep(2)
                            bot.find_product(i)
                            success = bot.cart(delay)
                    if success == 1:
                        print(colored("      Added to Cart!", "green"))
                    count += 1
                    time.sleep(0.5)
                bot.checkout(delay)
                exit(0)
            else:
                bot.main()


if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"
                      "CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "Trailers",
    }
    bot = Bot()
    menu = Menu()
    os.system("clear")
    menu.start()
