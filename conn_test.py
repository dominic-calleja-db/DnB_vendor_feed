

import requests  # pip install requests
import http.client
import json
import ast


"""
Authentication 
"""
conn = http.client.HTTPSConnection("plus.dnb.com")
payload = {"grant_type": "client_credentials"}
headers = {
    'accept': "application/json",
    'authorization': "Basic "+token,
    'content-type': "application/json",
}
conn.request("POST", "/v2/token", json.dumps(payload), headers)
res = conn.getresponse()
acc_dat = res.read()
print(acc_dat.decode("utf-8"))


acc_dat = ast.literal_eval(acc_dat.decode("utf-8"))
"""
Indentify
"""
duns_n = "551088438"

import http.client
 
conn = http.client.HTTPSConnection("plus.dnb.com")
headers = {
'accept': "application/json;charset=utf-8",
'authorization': "Bearer "+acc_dat['access_token'],
}
req_text = "https://plus.dnb.com/v1/data/duns/{}?blockIDs=companyinfo_L1_v1%2Cfinancialstrengthinsight_L1_v1&tradeUp=hq&customerReference=customer%20reference%20text&orderReason=6332".format(duns_n)
conn.request("GET",req_text , headers=headers)
res = conn.getresponse()
data = res.read()
print (data.decode("utf-8"))











