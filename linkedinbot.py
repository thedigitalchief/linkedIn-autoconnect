from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui as pag
import pylab 
import time


#defining variables
def main():
  url = "https://www.linkedin.com/"
  network_url = "https://linkedin.com/mynetwork/"
  driver = webdriver.Chrome("/usr/local/bin")
  start_bot(driver,url,network_url)
  driver.get(url)


#log in to the LinkedIn account
def login_to_linkedin(driver):
  username = driver.find_element_by_id("session_key")
  username.send_keys("me@dylanhnguyen.com")
  password = driver.find_element_bçy_id("session_password")
  password.send_keys("<password>")
  login_button = driver.find_element_by_class_name("sign-in-form__submit-button")
  login_button.click()


def goto_network_page(driver,network_url):
  driver.get(network_url)


def send_requests_to_users(driver):
  WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CLASS_NAME, "class name of an element"))
  )

  javaScript =  "window.scrollBy(0,4000);"
  driver.execute_script(javaScript)
  n =  int(input("Number of requests: "))

  for i in  range(0, n):
    pag.click(441, 666)
  print("Done!")


def take_a_screenshot(driver):
  loc_time = time.localtime()
  time_string = time.strftime("%m/%d/%Y", loc_time)
  driver.save_screenshot(time_string+"linkedinbot-screenshot.png")


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
def start_bot(driver,url,network_url):
  driver.get(url)
  login_to_linkedin(driver)
  goto_network_page(driver,network_url)
  send_requests_to_users(driver)
  accept_invitations_from_users(driver)

