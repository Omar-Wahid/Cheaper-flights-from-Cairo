import requests
from flight_search import FlightSearch

sheety_get_url = "https://api.sheety.co/1422412568980f150b651f7cd99f67aa/flightDeals/prices"
sheety_put_url = "https://api.sheety.co/1422412568980f150b651f7cd99f67aa/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.sheet_data = {}

    def get_data(self):
        response = requests.get(sheety_get_url)
        self.sheet_data = response.json()["prices"]
        print(self.sheet_data)
        return self.sheet_data

    def update_iataCode(self, sheet_data):
        flight_search = FlightSearch()
        if sheet_data[0]["iataCode"] == "":
            for row in self.sheet_data:
                row["iataCode"] = flight_search.get_code(row["city"])
                new_code = {
                    "price":{
                        "iataCode": row["iataCode"]
                    }
                }
                put_request = requests.put(f"{sheety_put_url}/{row['id']}", json=new_code)
                print(put_request.text)
