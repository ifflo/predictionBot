from unittest.mock import patch
from modules.common.price import get_price_from_binance, get_price_from_cryptocompare
import json
import unittest


class TestPriceModule(unittest.TestCase):

    @patch('modules.common.price.send_api_request')
    def test_get_price_from_binance_mocked(self, mock_send_request):
        mock_send_request.return_value = json.loads('{"symbol": "BTCUSDT", "price": "50000"}')
        price = get_price_from_binance('BTCUSDT')
        self.assertEqual(price, "50000")

    @patch('modules.common.price.send_api_request')
    def test_get_price_from_cryptocompare_mocked(self, mock_send_request):
        # Mock response data
        mock_response = {
            "USD": 50000
        }

        # Configure the mock to return a response with your mocked JSON data
        mock_send_request.return_value = mock_response

        # Call the function with the mock
        price = get_price_from_cryptocompare('BTC', 'USD')

        # Assert the expected outcome
        self.assertEqual(price, 50000)


if __name__ == '__main__':
    unittest.main()
