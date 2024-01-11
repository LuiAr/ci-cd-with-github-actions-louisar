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