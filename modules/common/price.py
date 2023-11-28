import requests
from config import BINANCE_API_KEY, CRYPTOCOMPARE_API_KEY
from utils.api_utils import send_api_request
from utils.rate_limiter import binance_limiter, cyptocompare_limiter


def get_price_from_binance(symbol):
    binance_limiter.wait()  # Wait if rate limit is reached
    url = f"https://api.binance.us/api/v3/ticker/price?symbol={symbol}"
    headers = {'X-MBX-APIKEY': BINANCE_API_KEY}
    data = send_api_request(url, headers=headers)
    return data['price'] if data else None


def get_price_from_cryptocompare(symbol, currency):
    cyptocompare_limiter.wait()  # Wait if rate limit is reached
    url = "https://min-api.cryptocompare.com/data/price"
    params = {'fsym': symbol, 'tsyms': currency}
    headers = {'Authorization': f'Apikey {CRYPTOCOMPARE_API_KEY}'}
    data = send_api_request(url, params=params, headers=headers)
    return data[currency] if data else None