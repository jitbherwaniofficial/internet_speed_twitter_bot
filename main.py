from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
load_dotenv()

PROMISED_DOWN = 100
PROMISED_UP = 100
 
TWITTER_EMAIL = os.environ["MY_EMAIL"]
TWITTER_PASSWORD = os.environ["MY_PASSWORD"]

class InternetSpeedTwitterBot:
    def __init__(self,DRIVER_PATH):
        self.DRIVER = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.DOWN = 0
        self.UP = 0

    def get_internet_speed(self,URL):
        self.DRIVER.get(URL)    
        self.DRIVER.maximize_window()
        # accept_btn = self.DRIVER.find_element_by_id("onetrust-accept-btn-handler").click()
        time.sleep(3)
        self.DRIVER.find_element_by_css_selector(".js-start-test").click()
        time.sleep(60)
        self.DOWN = self.DRIVER.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.UP = self.DRIVER.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        return f"DOWNLOAD SPEED: {self.DOWN}Mbps\nUPLOAD SPEED: {self.UP}Mbps"

    def tweet_at_provider(self,URL):
        self.DRIVER.get(URL)
        time.sleep(5)
        email = self.DRIVER.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(os.environ["MY_EMAIL"])
        next_ = self.DRIVER.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
        time.sleep(2)
        unusual_activity = self.DRIVER.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        unusual_activity.send_keys("@coderjit")
        unusual_activity.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.DRIVER.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(os.environ["MY_PASSWORD"])
        time.sleep(3)
        login = self.DRIVER.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
        time.sleep(5)
        # write_tweet_btn = self.DRIVER.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/svg')
        # write_tweet_btn.click()
        write_tweet = self.DRIVER.find_element(By.CSS_SELECTOR, 'div[data-contents="true"]')
        write_tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.DOWN}down/{self.UP}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        time.sleep(3)
        tweet_btn = self.DRIVER.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()
        time.sleep(5)
        self.DRIVER.quit()
        

bot = InternetSpeedTwitterBot(DRIVER_PATH=os.environ['CHROME_DRIVER_PATH'])        
SPEED = bot.get_internet_speed(URL="https://www.speedtest.net/")
print(SPEED)
time.sleep(2)
tweet = bot.tweet_at_provider(URL="https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D")

