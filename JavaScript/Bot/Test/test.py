from selenium import webdriver

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def main(self):
        self.driver.get("https://www.footlocker.com")

if __name__ == "__main__":
    bot = Bot()
    bot.main()
