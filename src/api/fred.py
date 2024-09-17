import requests
import os
import json
import logging
import dotenv

dotenv.load_dotenv()
LOG = logging.getLogger(__name__)
cwd = os.getcwd()

def get_latest_30_year_mortgage_rate() -> dict:
    """
    Get the latest 30 year mortgage rate
    """

    with open(f"{cwd}/cache/daily_fred_data.json", 'r') as file:
        data = json.load(file)
    return data['observations'][0] if data['observations'] else None


def get_fred_30_year_mortgage_rate():
    """
    Get the fred 30 year mortgage rate
    """
    hostname = "https://api.stlouisfed.org/fred/series/observations"
    params = {
    "series_id": "MORTGAGE30US",
    "api_key": os.getenv("FRED_API_KEY"),
    "file_type": "json",
    "sort_order": "desc",
    "observation_start": "2024-01-01",
    "frequency": "w"
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    try:
        print(params)
        response = requests.get(hostname, params=params, headers=headers)
    except Exception as e:
        print(e)
        return None
    
    return response.json()
    

    

