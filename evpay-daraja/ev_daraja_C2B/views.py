from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()
from django.views.decorators.csrf import csrf_exempt
from .access_token import generate_access_token
from .B2C_API import b2c_initialization
from .encoding_pass import generate_password
from .utils import get_time
from .stk_push import stk_implementation


class C2B_API(APIView):
    def get(self, request, format=None):
        date = get_time()
        token = generate_access_token()
        password = generate_password(date)
        
        return Response({"access_token":token, "password":password})
    def post(self, request, format=None):
        pass

def stk_push_payment(request):
    stk_push = stk_implementation()
    return JsonResponse(stk_push)


# function for registering C2B urls
def register_url(self,request,*args, **kwargs):
    token = generate_access_token()
    validation_url = os.getenv('C2B_VALIDATION_URL')
    confirmation_url = os.getenv('C2B_CONFIRMATION_URL')
    # shortcode = os.getenv('C2B_SHORT_CODE')
    url = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'ShortCode': '600998',
        'ResponseType': 'Completed',
        'ConfirmationURL': os.getenv('C2B_VALIDATION_URL'),
        'ValidationURL': os.getenv('C2B_CONFIRMATION_URL'),
    }
    response = requests.post(url, json=payload, headers=headers)
    return HttpResponse(response)

# function for simulating C2B API call to Daraja

def simulate_C2B_API(self,request,*args, **kwargs):
    url = os.getenv('C2B_SIMULATION_URL')
    token = generate_access_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'ShortCode': os.getenv('C2B_SHORT_CODE'),
        'CommandID': os.getenv('C2B_COMMAND_ID'),
        'Amount': os.getenv('C2B_TEST_AMOUNT'),
        'Msisdn': os.getenv('MPESA_TEST_MSISDN'),
        'BillRefNumber': os.getenv('C2B_BILLREFERENCENUMBER')
    }
    response = requests.post(url, json=payload, headers=headers).json()
    return JsonResponse(response)

@csrf_exempt
def validationURL(self,request,*args, **kwargs):
    data = request.body.decode('utf-8')
    with open('validation.txt', 'a') as file:
        file.write(data)
    # validation logic goes in here
    response = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(response)

# function for Validating C2B API payment response
@csrf_exempt
def confirmationURL(self,request,*args, **kwargs):
    data = request.body.decode('utf-8')
    with open('confirmation.txt', 'a') as file:
        file.write(data)
    # Save to Db and retun message to the user

    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }

    return JsonResponse({"Confirmation":context},)


# B2C daraja API
# simulation function
def simulate_B2C_API(self,request,*args, **kwargs):
    response = b2c_initialization()
    return JsonResponse(response)

# timeout function
@csrf_exempt
def timeoutRsponse(self,request,*args, **kwargs):
    data = request.body.decode('utf-8')
    with open('timeout_result.txt', 'a') as file:
        file.write(data)
    response = {'timeout':"Error"}
    return JsonResponse(response)

# B2C result response
@csrf_exempt
def resultResponse(self,request,*args, **kwargs):
    data = request.body.decode('utf-8')
    with open('b2cresult.txt', 'a') as file:
        file.write(data)
    response = {'Success':"success"}
    return JsonResponse(response)

