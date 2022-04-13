from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui as pag
import time


#defining variables
def main():
  url =  "http://linkedin.com/"
  network_url =  "http://linkedin.com/mynetwork/"
  driver = webdriver.Chrome()
  start_bot(driver,url,network_url)
  driver.get(url)


#log in to the LinkedIn account
def login_to_linkedin(driver):
  username = driver.find_element_by_id("session_key")
  username.send_keys("Your Email Goes Here")
  password = driver.find_element_by_id("session_password")
  password.send_keys("Your Password Goes Here")
  driver.find_element_by_class_name("sign-in-form__submit-button").click()


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
  print("Done !")

def take_a_screenshot(driver):
  loc_time = time.localtime()
  time_string = time.strftime("%m/%d/%Y", loc_time)
  driver.save_screenshot(time_string+"_screenshot.png")


def  accept_invitations_from_users(driver):
  javaScript =  "window.scrollBy(0,0);"
  driver.execute_script(javaScript)
  element_exists =  True
  while element_exists:
    try:
      driver.find_element_by_class_name("invitation-card__action-btn")
    except NoSuchElementException:
      element_exists =  False
    finally :
      if element_exists:
        driver.find_element_by_class_name("invitation-card__action-btn artdeco-button--secondary").click()
