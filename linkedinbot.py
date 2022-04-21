from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
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
    try:
        error = driver.find_element_by_id("error-for-password")
        if "Hmm, that's not the right password" in error.text:
            print("Wrong Password")
            return 0
        elif "Password must be 6 characters or more" in error.text:
            print("Short Password")
            return 0
    except NoSuchElementException:
        return 1
    else:
        return 0


def check_email():
  return 1

def check_credentials():
  return 0


def open_networks():
  driver.get(network_url)
  driver.maximize_window()


def send_requests():

    flag = 1
    count_skipped = 0
    requests = 0

    while flag:
        #Getting all button elements
        button_elements = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "artdeco-button__text", " " ))]')

        for i in button_elements:
            if i.text == 'Connect':
                try:
                    i.click()
                    print("Connection Request send")
                    requests += 1
                except:
                    print("Skipped", count_skipped)
                    try:
                        driver.find_element_by_class_name("artdeco-button ip-fuse-limit-alert__primary-action artdeco-button--2 artdeco-button--primary ember-view").click()
                    except NoSuchElementException:
                        pass
                    count_skipped += 1
                    if count_skipped == 4:
                        flag = 0
                sleep(1)
            if requests >= no_of_requests:
                break
        if requests >= no_of_requests:
            break

        # scrolls down webpage and refresh the button list
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(2.5)



def visibilty(company_name):

    driver.get("https://www.linkedin.com/company/" + company_name + "/people/")
 


if __name__ == '__main__':
  login_url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
  network_url = "https://www.linkedin.com/mynetwork/"

  # Taking user input to set credentials
  email = input("Enter your email: ")
  password = input("Enter your password: ")

  # Driver running
  driver = webdriver.Chrome()

    # Calling the login function
  login()

    # wrong email check condition is left.




    