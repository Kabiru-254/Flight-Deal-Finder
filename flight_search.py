import requests

KIWI_API_KEY = "Use your own API Key"

KIWI_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"

KIWI_HEADERS = {
    "apikey": KIWI_API_KEY,
}


class FlightSearch:
    def __init__(self):
        global KIWI_API_KEY

    def get_iata_code(self, city):
        code_parameters = {
            "term": city,
        }
        code_response = requests.get(url=KIWI_ENDPOINT, headers=KIWI_HEADERS, params=code_parameters)
        code_response.raise_for_status()
        data = code_response.json()
        return data["locations"][0]["code"]
