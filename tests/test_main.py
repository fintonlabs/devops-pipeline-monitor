import unittest
from unittest.mock import patch
from main import get_last_build_status

class TestMain(unittest.TestCase):

    @patch('main.requests.get')
    def test_get_last_build_status(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {'result': 'SUCCESS'}

        status = get_last_build_status()

        self.assertEqual(status, 'SUCCESS')

if __name__ == '__main__':
    unittest.main()