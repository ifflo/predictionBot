import requests


def call_api(url):
    # Generic function to call an API
    response = requests.get(url)
    return response.json()
