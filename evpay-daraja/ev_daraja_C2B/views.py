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
from .access_token import generate_access_token


class C2B_API(APIView):
    def get(self, request, format=None):
        token = generate_access_token()
        
        return Response({"access_token":token})
    def post(self, request, format=None):
        pass

# function for registering C2B urls
def register_url(request):
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
        'ShortCode': '601426',
        'ResponseType': 'Completed',
        'ConfirmationURL': "https://cab1-102-167-54-163.ngrok-free.app/confirmation",
        'ValidationURL': "https://cab1-102-167-54-163.ngrok-free.app/validationURL",
    }
    response = requests.post(url, json=payload, headers=headers).json()
    return JsonResponse(response)

# function for simulating C2B API call to Daraja

def simulate_C2B_API(request):
    # reg_url = register_url(request)
    # print(reg_url)
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
    print(os.getenv('C2B_SHORT_CODE'))
    print(os.getenv('C2B_COMMAND_ID'))
    print(os.getenv('C2B_TEST_AMOUNT'))
    print(os.getenv('MPESA_TEST_MSISDN'))
    print(os.getenv('C2B_BILLREFERENCENUMBER'))
    
    return JsonResponse(response)

def validationURL(request):
    response = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(response)

# function for Validating C2B API payment response
def confirmationURL(request): 

    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }

    return JsonResponse({"Confirmation":context},)

