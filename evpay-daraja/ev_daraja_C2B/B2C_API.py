import requests
from .access_token import generate_access_token
from dotenv import load_dotenv
load_dotenv()
import os

#function for requesting B2C initialization
def b2c_initialization():
    initiator_name = os.getenv('B2C_INITIATOR_NAME')
    securityCredential = os.getenv('B2C_SECURITY_CREDENTIAL')
    CommandID = os.getenv('B2C_COMMANDID')
    Amount = os.getenv('B2C_AMOUNT')
    PartyA = os.getenv('B2C_PARTY_A')
    PartyB = os.getenv('B2C_PARTY_B')
    Remarks = 'test Remarks'
    QueTimeOutURL = os.getenv('B2C_QUE_TIMEOUT_URL')
    ResultURL = os.getenv('B2C_RESULT_URL')
    Ocassion = 'Salary'
    url = os.getenv('B2C_REQUEST_URL')

    token = generate_access_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {    
        "InitiatorName": initiator_name,
        "SecurityCredential": securityCredential,
        "CommandID": CommandID,
        "Amount": Amount,
        "PartyA": PartyA,
        "PartyB": PartyB,
        "Remarks": Remarks,
        "QueueTimeOutURL": QueTimeOutURL,
        "ResultURL": ResultURL,
        "Occassion": Ocassion,
    }
    response = requests.post(url,json=payload,headers=headers).json()

    return response
