#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 16:56:32 2021

@author: cindy

API for the National Nutrient Database for Standard Reference.

Provides information concerning food products' nutritional profiles from databases such as SR Legacy, Foundational Foods and the USDA Global Branded Food Products Database. 

"""

import requests
import pandas as pd

# Need API Key to access data, attach API key to end of URL
dataresponse = requests.get('https://api.nal.usda.gov/fdc/v1/foods/list?dataType=Foundation,SR%20Legacy&pageSize=25&api_key=INSERTHERE')
dataresponse.json()

# Example of value in dataset
# [
#   {
#     "dataType": "Branded",
#     "description": "NUT 'N BERRY MIX",
#     "fdcId": 534358,
#     "foodNutrients": [
#       {
#         "number": 303,
#         "name": "Iron, Fe",
#         "amount": 0.53,
#         "unitName": "mg",
#         "derivationCode": "LCCD",
#         "derivationDescription": "Calculated from a daily value percentage per serving size measure"
#       }
#     ],
#     "publicationDate": "4/1/2019",
#     "brandOwner": "Kar Nut Products Company",
#     "gtinUpc": "077034085228",
#     "ndbNumber": "7954",
#     "foodCode": "27415110"
#   }
# ]

products = dataresponse.json()

productnames = products[10]















