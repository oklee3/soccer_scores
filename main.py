import requests
from prem import *

api_key = 'fa7bb5fd5de8461fb040abdb404b651a'
headers = {'X-Auth-Token': api_key}

# testing different functions
get_table(headers, 'PL')