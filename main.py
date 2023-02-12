from datetime import datetime, timedelta, date
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
data_manager.update_iataCode(sheet_data)

TODAY = date.today()
FROM = TODAY + timedelta(days=1)
TO = FROM + timedelta(days=6 * 30)

tomorrow = FROM.strftime("%d/%m/%Y")
six_months = TO.strftime("%d/%m/%Y")

ORIGIN_CITY_IATA = "CAI"

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months
    )


