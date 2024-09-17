import os
import json
from .api.fred import get_fred_30_year_mortgage_rate

cwd = os.getcwd()

def exec_daily():
    print("Running get_fred_30_year_mortgage_rate")
    response = get_fred_30_year_mortgage_rate()
    file_name = f"{cwd}/cache/daily_fred_data.json"
    with open(file_name, "w") as file:
        json.dump(response, file)
    print("Wrote daily_fred_data.json")

