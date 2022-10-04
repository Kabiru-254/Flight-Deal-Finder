from twilio.rest import Client
import requests

API_KEY = "Use your own API key"
twilio_account_sid = "Use your account SID"
auth_token = "Use your own Auth Token"


class NotificationManager:
    def __init__(self):
        self.twilio_client = Client(twilio_account_sid, auth_token)

    def send_message(self, details: dict):
        message = self.twilio_client.messages.create(
            from_='Your twilio number',
            to='Recipent number',
            body=f"Low price Alert! Only €{details['price']} to fly from {details['origin_city']}-"
                 f"{details['origin_airport']} to {details['destination_city']}-{details['destination_airport']} from "
                 f"{details['out_date']} to {details['return_date']}!"
        )
        print(message.status)
