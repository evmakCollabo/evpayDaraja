import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
load_dotenv()


#Function for generating access token used in API headers as authorization bearer.
def generate_access_token():
    mpesa_auth_url = os.getenv('ACCESS_TOKEN_URL')
    access_token = requests.get(mpesa_auth_url,auth = (HTTPBasicAuth(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET')))).json()
    
    return access_token['access_token']