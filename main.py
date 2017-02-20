from lib import mixpanel
import time
import os
import ConfigParser

if os.path.isfile('config.ini'):
    config = ConfigParser.RawConfigParser()
    config.read('config.ini')
    #print config['mixpanel']
    api_key = config.get('mixpanel', 'api_key')
    api_secret = config.get('mixpanel', 'api_secret')
else:
    api_key = raw_input("API Key: ")
    api_secret = raw_input("API Secret: ")

from_date = "2017-02-19"#raw_input("From Date: ")
to_date = time.strftime("%Y-%m-%d")#raw_input("To Date: ")
output_file = os.path.join(os.getcwd(), 'data', 'file.json')#raw_input("Output Filename: ")

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