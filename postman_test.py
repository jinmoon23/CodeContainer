import requests
import json

url = "https://openapi.koreainvestment.com:9443/uapi/overseas-price/v1/quotations/price?AUTH=&EXCD=NAS&SYMB=AAPL"

payload = ""
headers = {
  'content-type': 'application/json',
  'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0b2tlbiIsImF1ZCI6Ijc0MTUyNzI3LTY0NDgtNDU5Ni1iZWRmLTI2NGVmODE4ODgzOSIsInByZHRfY2QiOiIiLCJpc3MiOiJ1bm9ndyIsImV4cCI6MTczMTEzNTg5NSwiaWF0IjoxNzMxMDQ5NDk1LCJqdGkiOiJQU09NTUdqNTdvcHY0c2FEaUJlbFNwOXVzYXI5THRYZnVrbzIifQ.cMahyAH7dXENgHj5lTqlwHAAXRfUaxfmRHR5avak35NeIuaWcNNYVe6xLOzNBx373EwYD_d97L5JYg1BzoamIw',
  'appkey': 'PSOMMGj57opv4saDiBelSp9usar9LtXfuko2',
  'appsecret': 'U9M/qgAs2UMY24ZIzUnTAXsXVbEROIg7Sf9cHzJyAyqJRG2e1Aen93zC55X//tCHOMXcG13Mp9Kv1+laKCpKpm+sGo9htc7/dBxiwfCOufhr8R2iI0YW512W8ESiDU3AtFRYZnq9VcvEkMggYFCKhiyuZJGt61rxzGPjg1ixondJ52KwGRU=',
  'tr_id': 'HHDFS00000300'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())
