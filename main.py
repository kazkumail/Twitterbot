from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


PROMISED_DOWN = 150
PROMISED_UP = 10
service = Service("/Users/kumail/Documents/Development/chromedriver")


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        go_button = self.driver.find_element(By.CLASS_NAME, 'start-text')
        go_button.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, 'result-data-large.number.result-data-value.download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME, 'result-data-large.number.result-data-value.upload-speed').text
        print(f" Down: {self.down}, \n Up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(5)
        email_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        email_field.click()
        email_field.send_keys("kazkumail@gmail.com")
        time.sleep(3)

        next_button = self.driver.find_element(By. CLASS_NAME, 'css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu')
        next_button.click()

        time.sleep(3)

        username_field = self.driver.find_element(By.CLASS_NAME, 'r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu')
        username_field.send_keys("internetuser119")
        username_field.send_keys(Keys.RETURN)
        time.sleep(3)

        password_field = self.driver.find_element(By.CLASS_NAME, 'r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu')
        password_field.send_keys("testingpassword123")
        password_field.send_keys(Keys.RETURN)

        time.sleep(5)

        tweet_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_field.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 150 down and 10 up?")
        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet_button.click()


bot = InternetSpeedTwitterBot(service)
bot.get_internet_speed()
bot.tweet_at_provider()

