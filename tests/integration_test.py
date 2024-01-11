import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller_fix

class TestAppE2E(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chromedriver_autoinstaller_fix.install()  
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://localhost:5000')

    # def wait_for_element(self, by, value, timeout=10):
    #     return WebDriverWait(self.driver, timeout).until(
    #         EC.presence_of_element_located((by, value))
    #     )

    def test_add_and_delete_item(self):
        self.driver.get("http://127.0.0.1:5000/")
        self.driver.find_element(By.NAME, "item").click()
        self.driver.find_element(By.NAME, "item").send_keys("AddItem")
        self.driver.find_element(By.NAME, "item").send_keys(Keys.ENTER)
        self.driver.find_element(By.NAME, "new_item").click()
        self.driver.find_element(By.NAME, "new_item").send_keys("UpdateItem")
        self.driver.find_element(By.NAME, "new_item").send_keys(Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "Delete").click()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()




    # def test_add_and_delete_item(self):
    #     # Test adding an item
    #     self.wait_for_element(By.NAME, "item").click()
    #     self.driver.find_element(By.NAME, "item").send_keys("Test Item")
    #     self.driver.find_element(By.CSS_SELECTOR, "button").click()
    #     self.wait_for_element(By.NAME, "new_item").click()
    #     self.driver.find_element(By.NAME, "new_item").send_keys("Modified Item")
    #     self.driver.find_element(By.CSS_SELECTOR, "li button").click()
    #     self.wait_for_element(By.NAME, "item").click()
    #     self.driver.find_element(By.NAME, "item").send_keys("A new Item")
    #     self.driver.find_element(By.CSS_SELECTOR, ".container > form > button").click()
    #     self.wait_for_element(By.LINK_TEXT, "Delete").click()
    #     self.wait_for_element(By.LINK_TEXT, "Delete").click()