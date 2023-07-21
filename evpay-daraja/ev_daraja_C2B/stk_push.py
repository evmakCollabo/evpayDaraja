import requests
from .access_token import generate_access_token
from .encoding_pass import generate_password
from .utils import get_time
import os
from dotenv import load_dotenv
load_dotenv() 

def stk_implementation():
    url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    time = get_time()
    password = generate_password(time)
    token = generate_access_token()
    headers = headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {    
            "BusinessShortCode": os.getenv('BUSINESS_SHORT_CODE'),    
            "Password": password,    
            "Timestamp":time,    
            "TransactionType": os.getenv('STK_TRANSACTION_TYPE'),    
            "Amount": "1",    
            "PartyA": os.getenv('STK_PARTY_A'),    
            "PartyB": os.getenv('STK_PARTY_B'),    
            "PhoneNumber": os.getenv('STK_PHONE_NUMBER'),    
            "CallBackURL": os.getenv('STK_CALLBACK_URL'),    
            "AccountReference":"Test",    
            "TransactionDesc":"Test"
        }
    response = requests.post(url, json=payload, headers=headers).json()
    return response