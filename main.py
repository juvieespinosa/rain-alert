import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient



OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "5d1f58d09f7671dae5a0c5f127d351ab"
account_sid = "ACabd597df73d4fb47f5918c84cdfd07f9"
auth_token = "ae004d8677cd074f7e6d9707e8f52e99"

weather_params = {
    "lat": 37.338207,
    "lon": -121.886330,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

will_rain = False

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
   condition_code = (hour_data["weather"][0]["id"])
   if int(condition_code) < 700:
       will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️.",
        from_='+12283358736',
        to='+4085091491'
    )

    print(message.status)
