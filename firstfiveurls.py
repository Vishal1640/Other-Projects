from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class bcci():

    def test(self):
        
        href_link1 = []

        baseurl = "https://www.google.com/"

        driver = webdriver.Firefox()
    
        driver.implicitly_wait(10)

        driver.get(baseurl)

        xpath_for_google_search_text = '//input[@name="q"]'

        google_search = driver.find_element(By.XPATH, xpath_for_google_search_text)

        google_search.send_keys("india cricket team")

        google_search.send_keys(Keys.ENTER)

        # # 1st link

        elem1 = '//a[@href]//h3//parent::a'

        elem1 = driver.find_elements(By.XPATH, elem1)

        for elem in elem1:
            l = elem.get_attribute("href")
            if l not in href_link1:
                href_link1.append(l)

        print(href_link1)
        

ict = bcci()

ict.test()

