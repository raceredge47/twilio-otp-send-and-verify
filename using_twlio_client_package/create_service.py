# Using twilio python package
import os
from twilio.rest import Client


ACCOUNT_SID = ["Your Account SID"]       #Twilio Account SID
TOKEN = ["Your Token"]                   #Twilio Token
client = Client(ACCOUNT_SID, TOKEN)      #Create twilio client

# Step 1 :- create verification service 
service = client.verify.v2.services.create(
                                        friendly_name=["Name anything you want for this otp service"]
                                    )

print(service.sid)          #Service SID


SERVICE_SID =[f"Your Service SID {service.sid}"]      #Service SID

