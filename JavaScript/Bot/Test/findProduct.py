import json
import os
import re
import time
import webbrowser

import requests
from bs4 import BeautifulSoup
from termcolor import colored


class Menu:
    def __init__(self):
        self.products = json.load(open("products.json"))
        self.profile = json.load(open("profile.json"))

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
                print(colored("\nreturning to menu...\n", "red"))
                menu.start()
            else:
                print(colored("\nreturning to menu...\n", "red"))
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
            self.products = json.load(open("products.json"))
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
            products = {
                "number_of_products": number_of_products,
                "product 1": input("Product Name: "),
                "category 1": input("Enter Category: "),
                "color 1": input("Enter Product Color: "),
            }
        elif number_of_products == "2":
            products = {
                "number_of_products": number_of_products,
                "product 1": input("Product Name: "),
                "category 1": input("Enter Category: "),
                "color 1": input("Enter Product Color: "),
                "product 2": input("Product Name: "),
                "category 2": input("Enter Category: "),
                "color 2": input("Enter Product Color: "),
            }
        elif number_of_products == "3":
            products = {
                "number_of_products": number_of_products,
                "product 1": input("Product Name: "),
                "category 1": input("Enter Category: "),
                "color 1": input("Enter Product Color: "),
                "product 2": input("Product Name: "),
                "category 2": input("Enter Category: "),
                "color 2": input("Enter Product Color: "),
                "product 3": input("Product Name: "),
                "category 3": input("Enter Category: "),
                "color 3": input("Enter Product Color: "),
            }

        with open("products.json", "w") as f:
            json.dump(products, f)
        print()

        menu.start()

    def view_product(self):
        print()
        for key in self.products:
            if key != "number_of_products":
                capitalized_key = " ".join(k.capitalize() for k in key.split("_"))
                key_value = self.products[key]
                print("{}: {}".format(colored(capitalized_key, "magenta"), key_value))
        print()

        menu.start()

    def edit_profile(self):
        print()
        name = re.compile(r"[A-Z][a-z]*\s[A-Z][a-z]*(\s[A-Z])?")
        email = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
        phone = re.compile(r"(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}")
        address = re.compile(
            r"\d+[ ](?:[A-Za-z0-9.-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr|Rd|Blvd|Ln|St)\.?"
        )
        zipcode = re.compile(r"\d{5}")
        card = re.compile(r"(?:\d[ -]*?){13,16}")
        month = re.compile(r'"0[1-9]"|"1[0-2]"')
        year = re.compile(r'"20\d{2}"')
        cvv = re.compile(r'"\d{3}"')

        profile = {
            "name": input("Cardholder's Name: "),
            "email": input("Email: "),
            "phone": input("Phone: "),
            "address": input("Address: "),
            "zip": input("Zipcode: "),
            "card": input("Card Number: "),
            "month": input("Card Expiration Month: "),
            "year": input("Card Expiration Year: "),
            "cvv": input("Card CVV: "),
        }

        with open("profile.json", "w") as f:
            json.dump(profile, f)

        with open("autofill.js") as f:
            contents = f.read()
            with open("autofill.js", "w") as f:
                f.write(name.sub(profile["name"], contents))
        with open("autofill.js") as f:
            contents = f.read()
            with open("autofill.js", "w") as f:
                f.write(email.sub(profile["email"], contents))
        with open("autofill.js") as f:
            contents = f.read()
            with open("autofill.js", "w") as f:
                f.write(phone.sub(profile["phone"], contents))
        with open("autofill.js") as f:
            contents = f.read()
            with open("autofill.js", "w") as f:
                f.write(address.sub(profile["address"], contents))
        with open("autofill.js") as f:
            contents = f.read()
            with open("autofill.js", "w") as f:
                f.write(zipcode.sub(profile["zip"], contents))
        with open("autofill.js") as f:
            contents = f.read()
            with open("autofill.js", "w") as f:
                f.write(card.sub(profile["card"], contents))
        with open("autofill.js") as f:
            contents = f.read()
            with open("autofill.js", "w") as f:
                f.write(month.sub('"{}"'.format(profile["month"]), contents))
        with open("autofill.js") as f:
            contents = f.read()
            with open("autofill.js", "w") as f:
                f.write(year.sub('"{}"'.format(profile["year"]), contents))
        with open("autofill.js") as f:
            contents = f.read()
            with open("autofill.js", "w") as f:
                f.write(cvv.sub('"{}"'.format(profile["cvv"]), contents))
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
        self.products = json.load(open("products.json"))
        self.browser = webbrowser.get("chrome")

    def find_product(self, x):
        try:
            category = self.products[f"category {x}"].lower().replace("/", "_")

            r = requests.get(
                "{}{}/{}".format(self.base, self.shop_ext, category), headers=headers
            ).text
            soup = BeautifulSoup(r, "lxml")

            temp_tuple = []
            temp_link = []

            for link in soup.find_all("a", href=True):
                temp_tuple.append((link["href"], link.text))

            for i in temp_tuple:
                if (
                    self.products[f"product {x}"] in i[1]
                    or self.products[f"color {x}"] in i[1]
                ):
                    temp_link.append(i[0])

            self.final_link = list(
                set([x for x in temp_link if temp_link.count(x) == 2])
            )[0]
            return True
        except:
            return False

    def main(self):
        self.products = json.load(open("products.json"))
        products = list(range(1, int(self.products["number_of_products"]) + 1))
        found_product = False
        max_count = 10
        count = 0
        if not found_product and count < max_count:
            # print("---------------------------")
            print(colored("Looking for Product...", attrs=["bold"]))
            while not found_product and count < max_count:
                found_product = bot.find_product(1)
                count += 1
                time.sleep(0.2)
        if found_product:
            print(colored("Product found!", "green"))
            for i in products:
                bot.find_product(i)
                self.browser.open(f"{self.base}{self.final_link}")
            print(colored("Opening Chrome...done!", "cyan"))
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
