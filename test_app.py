import unittest
from flask import Flask
from app import app, conn  

class TestCRUDOperations(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

        # Create a test database
        self.test_cursor = conn.cursor()
        self.test_cursor.execute("CREATE TABLE IF NOT EXISTS test_users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), email VARCHAR(255), age INT)")

    def tearDown(self):
        # Drop the test database after tests
        self.test_cursor.execute("DROP TABLE IF EXISTS test_users")
        self.test_cursor.close()

    def test_create_user(self):
        # Test creating a user
        response = self.app.post('/users', json={'username': 'testuser', 'email': 'test@email.com', 'age': 25})
        self.assertEqual(response.status_code, 201)

    def test_get_all_users(self):
        # Test getting all users
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_user(self):
        # Test getting a specific user
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 404)

    def test_update_user(self):
        # Test updating a user
        response = self.app.put('/users/1', json={'username': 'updateduser', 'email': 'updated@email.com', 'age': 30})
        self.assertEqual(response.status_code, 200)

    def test_delete_user(self):
        # Test deleting a user
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()