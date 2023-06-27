# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC5b0fe034e64cb5d39e367781a60bdf70"
auth_token = "19671ae8cce68e10c35826dfd17a1788"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+18556409436",
  to="+16064251699"
)
print(message.sid)