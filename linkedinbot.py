from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from chromedriver_py import binary_path
import os, random, sys, time, re, csv, datetime
from configure import *
import pyautogui as pag
import pylab 
from time import sleep
import requests
import variables
import parsel

#System.setProperty("webdriver.chrome.driver","/Users/dylannguyen/Documents/Coding - Local/Projects/Automated LinkedIn Networking Bot/automated-linkedin-networking-bot")

# setting parameters so Chrome and webpage detect botting

#options = webdriver.ChromeOptions()
#options.add_argument("--no-sandbox")
#options.add_argument("--headless")
#options.add_argument("--window-size=1920,1080")
#options.add_argument("--disable-extensions")



#log in to the LinkedIn account
def login():
    driver.get(login_url)
    sleep(2)

    # Setting up login details
    email_element = driver.find_element_by_id('username')
    password_element = driver.find_element_by_id('password')
    # Sending Input in the field
    email_element.send_keys(email)
    password_element.send_keys(password)

    # Submitting the login request
    driver.find_element_by_xpath(
        '//*[contains(concat( " ", @class, " " ), concat( " ", "mercado-button--primary", " " ))]').click()


def check_password():


def check_email():


def check_credentials():


def open_networks():


def send_requests():


if __name__ == '__main__':

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
def start_bot(driver, url, network_url):
  driver.get(url)
  login(driver)
  goto_network_page(driver,network_url)
  send_requests_to_users(driver)
  accept_invitations_from_users(driver)


    