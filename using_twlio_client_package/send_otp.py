# Using twilio python package
import os
from twilio.rest import Client


ACCOUNT_SID = ["Your Account SID"]       #Twilio Account SID
TOKEN = ["Your Token"]                   #Twilio Token
SERVICE_SID =["Your Service SID"]      #Service SID

client = Client(ACCOUNT_SID, TOKEN)      #Create twilio client

# Step 2 :- Send otp 
verifications = client.verify \
                     .v2 \
                     .services(SERVICE_SID) \
                     .verifications \
                     .create(to=["Formatted phone Number"], channel='sms')    #[Please see document of all channel]

print(verification)     #Response Object
