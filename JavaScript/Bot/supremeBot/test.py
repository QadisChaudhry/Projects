import re

name = re.compile("[A-Z][a-z]*\s[A-Z][a-z]*(\s[A-Z])?")
email = re.compile("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
phone = re.compile("(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}")
address = re.compile("\d+[ ](?:[A-Za-z0-9.-]+[ ]?)+(?:Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr|Rd|Blvd|Ln|St)\.?")
zipcode = re.compile("\d{5}")
card = re.compile("(?:\d[ -]*?){13,16}")
month = re.compile('"0[1-9]"|"1[0-2]"')
year = re.compile('"20\d{2}"')
cvv = re.compile('"\d{3}"')

profile = {
    "name": input("Cardholder's Name: "),
    "email": input("Email: "),
    "phone": input("Phone: "),
    "address": input("Address: "),
    "zip": input("Zipcode: "),
    "card": input("Card Number: "),
    "month": input("Card Expiration Month: "),
    "year": input("Card Expiration Year: "),
    "cvv": input("Card CVV: ")
}

with open("test2.js") as f:
    contents = f.read()
    with open("test2.js", "w") as f:
        f.write(name.sub(profile["name"], contents))
with open("test2.js") as f:
    contents = f.read()
    with open("test2.js", "w") as f:
        f.write(email.sub(profile["email"], contents))
with open("test2.js") as f:
    contents = f.read()
    with open("test2.js", "w") as f:
        f.write(phone.sub(profile["phone"], contents))
with open("test2.js") as f:
    contents = f.read()
    with open("test2.js", "w") as f:
        f.write(address.sub(profile["address"], contents))
with open("test2.js") as f:
    contents = f.read()
    with open("test2.js", "w") as f:
        f.write(zipcode.sub(profile["zip"], contents))
with open("test2.js") as f:
    contents = f.read()
    with open("test2.js", "w") as f:
        f.write(card.sub(profile["card"], contents))
with open("test2.js") as f:
    contents = f.read()
    with open("test2.js", "w") as f:
        f.write(month.sub('"{}"'.format(profile["month"]), contents))
with open("test2.js") as f:
    contents = f.read()
    with open("test2.js", "w") as f:
        f.write(year.sub('"{}"'.format(profile["year"]), contents))
with open("test2.js") as f:
    contents = f.read()
    with open("test2.js", "w") as f:
        f.write(cvv.sub('"{}"'.format(profile["cvv"]), contents))

