import requests
from flight_search import FlightSearch


class DataManager:

    def __init__(self):
        self.data_list = []
        self.sheet_api = "Use your own API here"
        self.sheet_data = None
        self.data = None
        self.flight_searcher = FlightSearch()

    def get_sheet_data(self):
        self.sheet_data = requests.get(url=self.sheet_api)
        self.sheet_data.raise_for_status()
        self.data = self.sheet_data.json()
        self.data_list = self.data["prices"]
        return self.data_list

    def edit_sheet(self):
        for item in self.data_list:
            sheet_input = {
                "price": {
                    "iataCode": self.flight_searcher.get_iata_code(item["city"])
                }
            }
            sheet_response = requests.put(url=f"{self.sheet_api}/{item['id']}", json=sheet_input)
            # print(sheet_response.text)

