import os
import json
from .api.fred import get_fred_30_year_mortgage_rate
from .api.alphavantage import get_ipo_calendar

cwd = os.getcwd()

def exec_daily_fred_30_year_mortgage_rate():
    print("Running get_fred_30_year_mortgage_rate")
    response = get_fred_30_year_mortgage_rate()
    file_name = f"{cwd}/cache/daily_fred_data.json"
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(response, file)
    print("Wrote daily_fred_data.json")


def exec_daily_ipo_calendar():
    print("Running get_ipo_calendar")
    response = get_ipo_calendar()
    file_name = f"{cwd}/cache/daily_ipo_calendar.json"
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(response, file)
    print("Wrote daily_ipo_calendar.json")
    

def daily_refresh():
    exec_daily_fred_30_year_mortgage_rate()
    exec_daily_ipo_calendar()