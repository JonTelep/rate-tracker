import requests




def get_alpha_vantage_data():
    """
    Get the data from the zillow api
    """
    
    hostname = "https://mortgageapi.zillow.com/getRates"
    params = {
        "partnerId": "X1-ZWz19s19v6nidz_84h5s",
        
    }
    
    headers = {
        
    }

    response = requests.get(hostname, params=params, headers=headers)
    return response.json()
