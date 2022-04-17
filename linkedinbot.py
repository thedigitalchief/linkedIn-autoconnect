from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from chromedriver_py import binary_path
import pyautogui as pag
import pylab 
import time
import requests
import variables
import parsel

#System.setProperty("webdriver.chrome.driver","/Users/dylannguyen/Documents/Coding - Local/Projects/Automated LinkedIn Networking Bot/automated-linkedin-networking-bot")

#setting parameters so Chrome and webpage detect botting
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")


#defining variables

url = "https://www.linkedin.com/"
network_url = "https://linkedin.com/mynetwork/"
driver = webdriver.Chrome()
driver.get(url)


#log in to the LinkedIn account
def login_to_linkedin(driver):
  username = driver.find_element_by_id("session_key")
  username.send_keys("me@dylanhnguyen.com")
  password = driver.find_element_bçy_id("session_password")
  password.send_keys("<password>")
  driver.find_element_by_class_name("sign-in-form__submit-button").click()


def goto_network_page(driver,network_url):
  driver.get(network_url)


def google_search(driver, username, password):
  driver.get(variables.search_query)
  username.send_keys(variables.linkedin_username)
  password.send_keys(variables.linkedin_password)


def send_requests_to_users(driver):
  WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CLASS_NAME, "class name of an element"))
)
  javaScript =  "window.scrollBy(0,4000);"
  driver.execute_script(javaScript)
  n =  int(input("Number of requests: "))
  for i in  range(0, n):
    pag.click(441, 666)
  print("Done !")


def take_a_screenshot(driver):
  loc_time = time.localtime()
  time_string = time.strftime("%m/%d/%Y", loc_time)
  driver.save_screenshot(time_string+"_screenshot.png")


def accept_invitations_from_users(driver):
  javaScript =  "window.scrollBy(0,0);"
  driver.execute_script(javaScript)
  element_exists = True

  while element_exists:
    try:
      driver.find_element_by_class_name("invitation-card__action-btn")
    except NoSuchElementException:
      element_exists = False
    finally :
      if element_exists:
        driver.find_element_by_class_name("invitation-card__action-btn artdeco-button--secondary").click()


#connecting the functions and methods
def main(driver,url,network_url):
  start_bot(driver)
  login_to_linkedin(driver)
  goto_network_page(driver,network_url)
  send_requests_to_users(driver)
  accept_invitations_from_users(driver)

