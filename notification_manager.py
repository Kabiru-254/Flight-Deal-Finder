from twilio.rest import Client
import requests

API_KEY = "43acb4d7e845d481a06876384a2d0abe"
twilio_account_sid = "AC84013a64fc4b82e966fa50d6266a41c1"
auth_token = "9ba67f5874e000b9ef20da3dc42481b1"


class NotificationManager:
    def __init__(self):
        self.twilio_client = Client(twilio_account_sid, auth_token)

    def send_message(self, details: dict):
        message = self.twilio_client.messages.create(
            from_='+19897621146',
            to='+254724802599',
            body=f"Low price Alert! Only €{details['price']} to fly from {details['origin_city']}-"
                 f"{details['origin_airport']} to {details['destination_city']}-{details['destination_airport']} from "
                 f"{details['out_date']} to {details['return_date']}!"
        )
        print(message.status)
