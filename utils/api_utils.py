import requests
from utils.log_utils import setup_logger

logger = setup_logger('API Utils', 'api_utils.log')


def send_api_request(url, params=None, headers=None):
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"API request error: {e}")
        return None

