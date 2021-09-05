import requests
import time
import os
import json
import pyautogui as pg
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
        elif selection == ".":
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

    def find_product(self, x):
        try:
            r = requests.get("{}{}/{}".format(self.base, self.shop_ext, self.product[f"category{x}"]),
                             headers=headers).text
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

    def open_gmail(self):
        pg.hotkey("command", "space")
        pg.typewrite("sa\n")
        pg.hotkey("command", "t")
        pg.typewrite("https://gmail.com\n", 0.03)
        time.sleep(3)
        pg.hotkey("command", "shift", "a")
        time.sleep(3)
        pg.press("enter")
        time.sleep(3)
        pg.hotkey("command", "shift", "a")

    def product_page(self):
        pg.hotkey("command", "t")
        pg.typewrite(f"{self.base}{self.final_link}\n", 0.02)
        time.sleep(3)

    def cart(self):
        s = pg.locateOnScreen("atc_image.png", confidence=0.7)
        pg.moveTo(pg.center(s))
        pg.click()
        time.sleep(0.5)

        s = pg.locateOnScreen("checkout_image.png", confidence=0.9)
        pg.moveTo(pg.center(s))
        pg.click()
        time.sleep(1)

    def checkout(self):
        pg.moveTo(1150, 495)
        pg.click()
        pg.typewrite(self.profile["name"])
        pg.press("tab")

        pg.typewrite(self.profile["email"])
        pg.press("tab")

        pg.typewrite(self.profile["phone"])
        pg.press("tab")

        pg.typewrite(self.profile["address"])
        pg.press("tab", 2)

        pg.typewrite(self.profile["zip"])

        pg.press("tab", 5)

        pg.typewrite(self.profile["card"])
        pg.press("tab", 3)

        pg.typewrite(self.profile["cvv"])

        pg.moveTo(1400, 730)
        pg.click()
        pg.press("enter")

    def main(self):
        start = time.time()
        bot.find_product(1)
        bot.open_gmail()
        # bot.product_page()
        # bot.cart()
        # bot.checkout()
        end = time.time()
        print(f"{round(end - start, 4)}")


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
    pg.PAUSE = .2
    # os.system("clear")
    bot.main()
