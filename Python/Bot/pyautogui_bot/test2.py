import webbrowser
import requests
import time
import os
import pyautogui as pg
import json
from termcolor import colored
from bs4 import BeautifulSoup


class Menu:
    def __init__(self):
        self.profile = json.load(open("profile1.json"))
        self.product = json.load(open("products1.json"))

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
            self.product = json.load(open("products1.json"))
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
            self.profile = json.load(open("profile1.json"))
            menu.view_profile()
            menu.start()
        else:
            print(colored("\nEnter a Valid Selection", "red"))
            menu.profile_menu()

    def enter_product(self):
        number_of_products = input("\nNumber of Products (1-3): ")

        if number_of_products == "1":
            products = {"number_of_products": number_of_products,
                        "product1": input("Product Name: "),
                        "category1": input("Enter Category: "),
                        "color1": input("Enter Product Color: ")}
        elif number_of_products == "2":
            products = {"number_of_products": number_of_products,
                        "product1": input("Product Name: "),
                        "category1": input("Enter Category: "),
                        "color1": input("Enter Product Color: "),
                        "product2": input("Product Name: "),
                        "category2": input("Enter Category: "),
                        "color2": input("Enter Product Color: ")}
        elif number_of_products == "3":
            products = {"number_of_products": number_of_products,
                        "product1": input("Product Name: "),
                        "category1": input("Enter Category: "),
                        "color1": input("Enter Product Color: "),
                        "product2": input("Product Name: "),
                        "category2": input("Enter Category: "),
                        "color2": input("Enter Product Color: "),
                        "product3": input("Product Name: "),
                        "category3": input("Enter Category: "),
                        "color3": input("Enter Product Color: ")}
        else:
            print(colored("\nEnter Number From 1-3", "red"))
            menu.enter_product()

        with open("products1.json", "w") as f:
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

        with open("profile1.json", "w") as f:
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
        self.shop_ext = "/shop/all"
        self.checkout_ext = "/checkout"
        self.product = json.load(open("products1.json"))
        self.profile = json.load(open("profile1.json"))
        self.browser = webbrowser.get("chrome")

    def find_product(self, x):
        try:
            category = self.product[f"category{x}"].lower().replace("/", "_")

            r = requests.get("{}{}/{}".format(self.base, self.shop_ext, category), headers=headers).text
            soup = BeautifulSoup(r, "lxml")

            temp_tuple = []
            temp_link = []

            for link in soup.find_all("a", href=True):
                temp_tuple.append((link["href"], link.text))

            for i in temp_tuple:
                if self.product[f"product{x}"] in i[1] or self.product[f"color{x}"] in i[1]:
                    temp_link.append(i[0])

            self.final_link = list(set([x for x in temp_link if temp_link.count(x) == 2]))[0]
            return True
        except:
            return False

    def cart(self):
        self.browser.open(f"{self.base}{self.final_link}")
        time.sleep(2)
        s = pg.locateOnScreen("atc_image.png", confidence=0.7)
        while s is None:
            s = pg.locateOnScreen("atc_image.png", confidence=0.7)
        pg.moveTo(pg.center(s))
        time.sleep(0.2)
        pg.click()
        print(colored("      Added to Cart!", "green"))
        time.sleep(0.3)

    def checkout(self):
        print(colored("Checkout", attrs=["bold"]))
        self.browser.open(f"{self.base}{self.checkout_ext}")
        time.sleep(0.5)
        print(colored("  Checking Out...", "white"))
        time.sleep(2)

        pg.click(1150, 495, 1, 0.2)
        time.sleep(1)
        pg.typewrite(self.profile["name"])
        time.sleep(0.2)
        pg.press("tab", 1)
        time.sleep(0.2)
        pg.typewrite(self.profile["email"])
        time.sleep(0.2)
        pg.press("tab", 1)
        time.sleep(0.2)
        pg.typewrite(self.profile["phone"])
        time.sleep(0.2)
        pg.press("tab", 1)
        time.sleep(0.2)
        pg.typewrite(self.profile["address"])
        time.sleep(0.2)
        pg.press("tab", 2)
        time.sleep(0.2)
        pg.typewrite(self.profile["zip"])
        time.sleep(0.2)
        pg.press("tab", 5)
        time.sleep(0.2)
        pg.typewrite(self.profile["card"])
        time.sleep(0.2)
        pg.press("tab", 3)
        time.sleep(0.2)
        pg.typewrite(self.profile["cvv"])

        time.sleep(0.5)
        pg.click(1440, 570)
        time.sleep(0.2)
        pg.click(1435, 450)
        time.sleep(0.5)
        pg.click(1500, 570)
        time.sleep(0.2)
        pg.click(1490, 615)

        time.sleep(0.5)
        pg.click(1430, 735)
        time.sleep(0.2)

        pg.click(1660, 825)
        print(colored("  Checkout Succeeded!", "green"))

    def main(self):
        self.product = json.load(open("products1.json"))
        self.profile = json.load(open("profile1.json"))
        products = list(range(1, int(self.product['number_of_products']) + 1))
        found_product = False
        max_count = 10
        count = 0
        if not found_product and count < max_count:
            print("---------------------------")
            print(colored("Looking for Product...", attrs=["bold"]))
            while not found_product and count < max_count:
                found_product = bot.find_product(1)
                count += 1
                time.sleep(0.2)
        if found_product:
            print(colored("Product Found!", "green"))
            start = time.time()
            count = 1
            print(colored("Cart", attrs=["bold"]))
            for i in products:
                bot.find_product(i)
                print(colored(f"  ({count}) Adding to Cart...", "white"))
                count += 1
                bot.cart()
                time.sleep(1.2)
            # bot.checkout()
            end = time.time()
            print(colored(f"  Run time: {round(float(end - start), 4)} seconds\n", "cyan"))
            exit(0)
        else:
            bot.main()


if __name__ == "__main__":
    pg.PAUSE = 0.25
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
