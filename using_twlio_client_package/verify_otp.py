# Using twilio python package
import os
from twilio.rest import Client


ACCOUNT_SID = ["Your Account SID"]       #Twilio Account SID
TOKEN = ["Your Token"]                   #Twilio Token
SERVICE_SID =["Your Service SID"]      #Service SID

client = Client(ACCOUNT_SID, TOKEN)      #Create twilio client

verification_checks = client.verify \
                     .v2 \
                     .services(SERVICE_SID) \
                     .verification_checks \
                     .create(to=['OTP Received Phone Number'], code=['Enter Received OTP'])

print(verification)     #Response Object
