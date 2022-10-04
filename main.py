from pprint import pprint
from datetime import timedelta, datetime
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
data_list = data_manager.get_sheet_data()

flight_searcher = FlightSearch()
sms_manager = NotificationManager()

for item in data_list:
    if not item["iataCode"]:
        iata = flight_searcher.get_iata_code(item["city"])


date_today = datetime.now().strftime("%d/%m/%Y")
six_months_date = (datetime.now() + timedelta(days=6 * 30)).strftime("%d/%m/%Y")

flight_data = FlightData()
code_list = flight_data.get_code_list()

available_flights = []
for code in code_list:
    KIWI_SEARCH_PARAMETERS = {
        "fly_from": "LON",
        "fly_to": code,
        "dateFrom": date_today,
        "dateTo": six_months_date,
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "one_for_city": 1,
        "max_stopovers": 0,
        "curr": "GBP"
    }
    city_dict = flight_data.get_prices(KIWI_SEARCH_PARAMETERS)
    available_flights.append(city_dict)


for item in available_flights:
    if item:
        sms_manager.send_message(item)
