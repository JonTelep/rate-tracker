"""Main app"""

from .api.fred import get_latest_30_year_mortgage_rate, get_fred_30_year_mortgage_rate
from .daily import daily_refresh

daily_refresh()

latest_30_year_mortgage_rate = get_latest_30_year_mortgage_rate()
print(f"Latest 30 year mortgage rate: {latest_30_year_mortgage_rate}")

