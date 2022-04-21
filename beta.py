import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LinkedinBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome('/Users/dylannguyen/Documents/Coding - Local/Projects/Automated LinkedIn Networking Bot/automated-linkedin-networking-bot')
        time.sleep(1)

        self.base_url = 'https://www.linkedin.com'
        self.login_url = self.base_url + '/login'
        self.feed_url = self.base_url + '/feed'

        self.username = username
        self.password = password

    def _nav(self, url):
        self.driver.get(url)
        time.sleep(2)

    def login(self, username, password):
        self._nav(self.login_url)
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('password').send_keys(self.password)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()

    def search(self, text, connect=False):
        # self._nav(self.feed_url)
        time.sleep(1)
        search = self.driver.find_element_by_class_name('search-global-typeahead__input')
        search.send_keys(text)
        search.send_keys(Keys.ENTER)
        
        time.sleep(3)
        self.driver.find_element_by_class_name('search-vertical-filter__filter-item-button').click()
        time.sleep(3)

        if connect:
            self._search_connect()

    def _search_connect(self):        
        count=0

        connect = self.driver.find_elements_by_css_selector('button.search-result__action-button')
        for i in connect:
            count+=1
            i.click()
            time.sleep(1)
            self.driver.find_element_by_css_selector('button.mr1').click()
            customMessage = "Hello, I have found mutual interest fields in your profile would very much like to learn more about your career path. I hope you will consider connecting!!"
            elementID = self.driver.find_element_by_id('custom-message')
            elementID.send_keys(customMessage)
            time.sleep(2)
            self.driver.find_element_by_class_name('ml1').click()
            time.sleep(1)
            if count>5:
                break


if __name__ == '__main__':

    file = open('config.txt')
    lines = file.readlines()
    username = lines[0]
    password = lines[1]

    search_text = 'Google'

    bot = LinkedinBot(username, password)
    bot.login(username, password)
    bot.search(search_text, connect=True)

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
