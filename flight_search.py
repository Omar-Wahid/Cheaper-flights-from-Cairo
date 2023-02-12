import requests
from flight_data import FlightData
from pprint import pprint

APIKEY = "T9JYWGFsMOieL4ckF4hMtKV67pPwiwxp"
ENDPOINT = "https://api.tequila.kiwi.com"
KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"



class FlightSearch:
    def get_code(self, city):
        location_endpoint = f"{ENDPOINT}/locations/query"
        headers = {"apikey": APIKEY}
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": APIKEY}
        query = {
            "fly_from": origin_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "fly_to": destination_city_code,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EGP"
        }

        response = requests.get(url=KIWI_ENDPOINT, headers=headers, params=query)

        try:
            data = response.json()["data"][0]
            print(data)
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        pprint(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data