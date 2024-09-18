import requests
import os
import json

def get_ipo_calendar():
    """
    Get the ipo calendar from the alpha vantage api
    """
    hostname = "https://www.alphavantage.co/query"
    params = {
        "function": "IPO_CALENDAR",
        "apikey": os.getenv("ALPHA_VANTAGE_API_KEY")
    }
    response = requests.get(hostname, params=params, timeout=10)
    return response.json()

