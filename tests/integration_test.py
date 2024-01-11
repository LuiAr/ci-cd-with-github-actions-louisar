import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def waitAbit():
    time.sleep(1)

class TestAppE2E(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage") 
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://localhost:5000')

    def test_add_and_delete_item(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.find_element(By.NAME, "item").click()
        waitAbit()
        self.driver.find_element(By.NAME, "item").send_keys("AddItem")
        waitAbit()
        self.driver.find_element(By.NAME, "item").send_keys(Keys.ENTER)
        waitAbit()
        self.driver.find_element(By.NAME, "new_item").click()
        waitAbit()
        self.driver.find_element(By.NAME, "new_item").send_keys("UpdateItem")
        waitAbit()
        self.driver.find_element(By.NAME, "new_item").send_keys(Keys.ENTER)
        waitAbit()
        self.driver.find_element(By.LINK_TEXT, "Delete").click()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
