# Using pyhton requests package

from requests.auth import HTTPBasicAuth
import requests

ACCOUNT_SID = ["Your Account SID"]       #Twilio Account SID
TOKEN = ["Your Token"]                   #Twilio Token
SERVICE_SID =[f"Your Service SID {service.sid}"]      #Service SID

# Verify Twilio OTP
send_otp_url = f'''https://verify.twilio.com/v2/Services/{SERVICE_SID}/VerificationCheck'''
data = {
    'To': ['Formatted Phone Number'],
    'Code':['Received otp']   
    }
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

res = requests.post(url=send_otp_url, auth= HTTPBasicAuth(ACCOUNT_SID, TOKEN),
                 headers = headers,
                 data= data
               )

print(res.json())       #Response