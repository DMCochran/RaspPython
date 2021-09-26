# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import requests
#import json
import pandas as pd
from datetime import date

startDate = '2020-05-01'
endDate = date.today().strftime("%Y-%m-%d")

url='https://data.ca.gov/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%2242d33765-20fd-44b8-a978-b083b7542225%22%20WHERE%20%22todays_date%22%20BETWEEN%20%27'+startDate+'%27%20AND%20%27'+endDate+'%27'
#header= {'user-agent': '(glitchlabs.org, david@glitchlabs.org)'}

#r=requests.get(url,headers=header)
#r=requests.get(url)
result = pd.read_json(url)
bedData = result['records']
print(bedData)
#print(df.)
