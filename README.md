# evpayDaraja

EVPay-Safaricom Integration is a comprehensive payment solution that seamlessly integrates with Safaricom's M-PESA platform, offering a streamlined experience for handling STK Push, C2B (Customer to Business), and B2C (Business to Customer) transactions. This project is built using Python, empowering businesses to securely and efficiently process payments through M-PESA.

## Key Features
 * STK Push : Enable customers to make payments directly from their mobile phones with a simple USSD prompt.
 * C2B (Customer to Business): Easily accept payments from customers initiated by their mobile money accounts.
 * B2C (Business to Customer): Effortlessly disburse funds to multiple recipients' M-PESA accounts.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What software you need to install and how to install them

- [Python3](https://www.python.org/downloads/)
- [Python Virtual Environment, virtualenv](https://docs.python.org/3/tutorial/venv.html)
- [Django](https://docs.djangoproject.com/en/4.1/intro/install/)
- [PostgreSQL](https://docs.postgresql.org) and [psycopg](https://www.psycopg.org/)
- Any other dependencies listed in requirements.txt

### Installing

A step by step series of examples that tell you how to get a development env running

1. Clone the repository using

`git clone https://github.com/evmakCollabo/evpayDaraja.git`

OR

 `git clone git@github.com:evmakCollabo/evpayDaraja.git` if using SSH

2. You need to activate a virtual environment for the project, and every other time you want to make changes

 Here, [venv](https://docs.python.org/3/tutorial/venv.html) is included with python.

 Start with `python3 -m venv [replace with what you would like to call the virtual environment]`. You can do `python3 -m venv evpay`

 Activate virtual environment using what you call your virtual environment. Our example is `evpay`

`source evpay/bin/activate`

 Then navigate to the relevant directory and install requirements using `pip install -r requirements.txt`

 If you are using Windows and encounter an error, then try the below process:
 Go to the terminal - Step 1:
 `pip3 install -U pip virtualenv`
 Step 2:
 `virtualenv --system-site-packages -p python ./venv`
 or
 `virtualenv --system-site-packages -p python3 ./venv`
 Step 3:
 `.\venv\activate`


3. Run migrations

`python manage.py makemigrations`

`python manage.py migrate`

4. generate a new SECRET_KEY and update your Django project's configuration. To do this:
- Open a Python shell by running the following command in your project's directory:
 Run `python manage.py shell`

- Execute the following command to generate a new SECRET_KEY:
```
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
- Copy the generated value and add it to your .env file

5. Run the server, inside `project-evpayDaraja/evpay-daraja/`

`python manage.py runserver`

The server will be running on <http://127.0.0.1:8000/>

## Running the tests

We will update this part once we start writing tests for the code

`python manage.py test`

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Python](https://www.python.org/) - Programming Language

## Authors (Add Your Own)

- **[Paulo Akello](https://github.com/blackoaz)** -
- **[Lucy Maina](https://github.com/NjeriMaina4172)** -
- **[Vanessa Ojuok](https://github.com/Vanessaojuok)** -
- **[Michael Bahati](https://github.com/Manenomyk)** -
## License

This project is licensed under the [MIT](link) - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Any acknowledgements go here
