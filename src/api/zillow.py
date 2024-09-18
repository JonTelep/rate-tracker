import requests
import os
cwd = os.getcwd()

def get_alpha_vantage_data():
    """
    Get the data from the zillow api
    """
    
    hostname = "https://mortgageapi.zillow.com/getRates"
    params = {
        "partnerId": os.getenv("ZILLOW_API_KEY"),
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"        
    }

    response = requests.get(hostname, params=params, headers=headers, timeout=10)
    return response.json()
