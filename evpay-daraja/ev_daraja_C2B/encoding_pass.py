import base64
import os
from dotenv import load_dotenv
load_dotenv()


def generate_password(date):
    encoding_data = os.getenv('BUSINESS_SHORT_CODE') + os.getenv('LIPANAMPESA_PASSKEY') + date
    encoded_string = base64.b64encode(encoding_data.encode())
    decoded_password = encoded_string.decode("utf-8")
    return decoded_password
