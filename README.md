SMS RAIN ALERT APP

A rain alert program, written in Python, that notifies in the morning via SMS  of anticipated rain chances using OpenWeather API.

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
