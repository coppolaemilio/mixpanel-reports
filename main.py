from lib import mixpanel
import time
import os

api_key = raw_input("API Key: ")
api_secret = raw_input("API Secret: ")

from_date = "2017-01-01"#raw_input("From Date: ")
to_date = time.strftime("%Y-%m-%d")#raw_input("To Date: ")
output_file = os.path.join('data', 'file.json')#raw_input("Output Filename: ")

api = mixpanel.Mixpanel(
    api_key = api_key, 
    api_secret = api_secret,
    output_file = output_file
)

data = api.request(['export'], {
    'event': ['Modal'],
    'from_date': from_date,
    'to_date': to_date,
    })