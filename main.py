from linebot import LineBotApi
from linebot.models import TextSendMessage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import os
import sys
import time
import datetime
import dotenv

HEADLESS = True

dotenv.load_dotenv()

URL = os.getenv('URL')
ID = os.getenv('ID')
PASS = os.getenv('PASS')
CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN')

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
  options = Options()

  if HEADLESS:
    options.add_argument('--headless')
  else:
    options.add_experimental_option("detach", True)

  with webdriver.Chrome(options=options) as driver:
    driver.get(URL)

    # ID
    id = driver.find_element(By.NAME, 'USERID')
    id.send_keys(ID)

    # Password
    password = driver.find_element(By.NAME, 'USERPASSWD')
    password.send_keys(PASS)

    time.sleep(3)

    # Login
    login = driver.find_element(By.XPATH, "//input[@value='ログイン']")
    login.click()
    print("Logged in:        ", time.ctime())

    time.sleep(3)

    # Car type
    select = driver.find_element(By.XPATH, "//input[@value='この車種を選択']")
    select.click()
    print("Car type selected:", time.ctime())

    prev_free = []

    # Update
    while True:
      dt_now = datetime.datetime.now()

      if dt_now.hour < 7 or dt_now.hour >= 19:
        break

      free = driver.find_elements(By.XPATH, "//td[@class='Free']")

      if len(free) > 0 and len(prev_free) == 0:
        print("Free detected!:   ", time.ctime())
        messages = TextSendMessage(text="予約に空きがあります！\n" + URL)
        line_bot_api.broadcast(messages=messages)

      time.sleep(150)
      update = driver.find_element(By.XPATH, "//input[@id='button']")
      update.click()
      prev_free = free
      print("Updated:          ", time.ctime())

if __name__ == '__main__':
  dt_now = datetime.datetime.now()

  if dt_now.hour < 7 or dt_now.hour >= 19:
    print("Error: Out of hours")
    sys.exit(1)

  main()