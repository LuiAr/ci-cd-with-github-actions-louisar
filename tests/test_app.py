# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time

# def waitAbit():
#     time.sleep(1)

# class TestAppE2E(unittest.TestCase):
#     def setUp(self):
#         # Launch your flask app first
#         chrome_options = Options()
#         chrome_options.binary_location = r"PATH/chromedriver.exe"
#         self.driver = webdriver.Chrome(options=chrome_options)
#         self.driver.get('http://localhost:5000')

#     def test_add_and_delete_item(self):
#         self.driver.get("http://127.0.0.1:5000/")
#         self.driver.find_element(By.NAME, "item").click()
#         waitAbit()
#         self.driver.find_element(By.NAME, "item").send_keys("AddItem")
#         waitAbit()
#         self.driver.find_element(By.NAME, "item").send_keys(Keys.ENTER)
#         waitAbit()
#         self.driver.find_element(By.NAME, "new_item").click()
#         waitAbit()
#         self.driver.find_element(By.NAME, "new_item").send_keys("UpdateItem")
#         waitAbit()
#         self.driver.find_element(By.NAME, "new_item").send_keys(Keys.ENTER)
#         waitAbit()
#         self.driver.find_element(By.LINK_TEXT, "Delete").click()



#     def tearDown(self):
#         self.driver.close()

# if __name__ == '__main__':
#     unittest.main()

import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_read_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")


    def test_add_item(self):
        response = self.app.post('/add', data=dict(item="Test Item"), follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
        self.assertIn(b'Test Item', response.get_data(), "Response should contain 'Test Item'")

    def test_delete_item(self):
        response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
        self.assertNotIn(b'Test Item', response.get_data(), "Response should not contain 'Test Item'")

        
    def test_update_item(self):
        self.app.post('/add', data=dict(item="Test Item"), follow_redirects=True)
        response = self.app.post('/update/0', data=dict(new_item="New Item"), follow_redirects=True)
        self.assertEqual(response.status_code, 200, "Response should be 200 OK")
        self.assertIn(b'New Item', response.get_data(), "Response should contain 'New Item'")
        self.assertNotIn(b'Test Item', response.get_data(), "Response should not contain 'Test Item'")


if __name__ == '__main__':
    unittest.main()