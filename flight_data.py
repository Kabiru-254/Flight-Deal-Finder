from data_manager import DataManager
import requests
from datetime import timedelta, datetime

KIWI_API_KEY = "R5C0eL-3cgfIJ1f03C6rzAmcVhVCVF9Z"
KIWI_HEADERS = {
    "apikey": KIWI_API_KEY,
}

KIWI_SEARCH_API = "https://tequila-api.kiwi.com/v2/search"


class FlightData:
    def __init__(self):
        self.price = None
        self.origin_city = None
        self.origin_airport = None
        self.destination_city = None
        self.destination_airport = None
        self.out_date = None
        self.return_date = None
        data_manager = DataManager()
        self.flight_list = data_manager.get_sheet_data()

    def get_code_list(self):
        code_list = []
        for item in self.flight_list:
            iata_code = item["iataCode"]
            code_list.append(iata_code)
        return code_list

    def get_prices(self, paramz):
        data_from_api = requests.get(url=KIWI_SEARCH_API, params=paramz, headers=KIWI_HEADERS)
        data_from_api.raise_for_status()
        data = data_from_api.json()["data"]

        if data:
            self.destination_city = data[0]["cityTo"]
            self.origin_city = data[0]["cityFrom"]
            self.price = data[0]["price"]
            self.origin_airport = data[0]["flyFrom"]
            self.destination_airport = data[0]["flyTo"]
            self.out_date = data[0]["route"][0]["local_departure"].split("T")[0]
            self.return_date = data[0]["route"][0]["local_departure"].split("T")[0]

            city_data = {
                "destination_city": self.destination_city,
                "origin_city": self.origin_city,
                "price": self.price,
                "origin_airport": self.origin_airport,
                "destination_airport": self.destination_airport,
                "out_date": self.out_date,
                "return_date": self.return_date
            }

            return city_data

        else:
            print(f"No flights available for {paramz}")
