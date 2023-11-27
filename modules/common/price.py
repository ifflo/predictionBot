import requests


def get_current_price(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

        data = response.json()
        # Assuming the API returns a JSON object with the price in a 'current_price' field
        return data['current_price']
    except requests.RequestException as e:
        print(f"Error fetching price data: {e}")
        return None
