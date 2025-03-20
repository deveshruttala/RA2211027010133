import requests
from django.utils.timezone import now

TEST_SERVER_BASE_URL = "http://20.244.56.144/test/"

CATEGORY_MAPPING = {
    'p': 'primes',
    'f': 'fibo',
    'e': 'even',
    'r': 'rand',
}

WINDOW_SIZE = 10

def fetch_numbers(category):
    if category not in CATEGORY_MAPPING:
        return []
    url = f"{TEST_SERVER_BASE_URL}{CATEGORY_MAPPING[category]}"
    try:
        response = requests.get(url, timeout=0.5)
        if response.status_code == 200:
            return response.json().get("numbers", [])
    except requests.exceptions.RequestException:
        return []
    return []
