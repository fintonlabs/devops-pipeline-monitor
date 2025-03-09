import unittest
from main import app

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_pipelines(self):
        response = self.app.get('/pipelines')
        self.assertEqual(response.status_code, 200)

    def test_post_pipelines(self):
        response = self.app.post('/pipelines', json={})
        self.assertEqual(response.status_code, 200)

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()