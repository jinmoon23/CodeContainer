import websockets
import json
import requests
import os
import asyncio
import time
from datetime import datetime

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def get_approval(key, secret):
    url = 'https://openapi.koreainvestment.com:9443'
    headers = {"content-type": "application/json"}
    body = {"grant_type": "client_credentials",
            "appkey": key,
            "secretkey": secret}
    PATH = "oauth2/Approval"
    URL = f"{url}/{PATH}"
    time.sleep(0.05)
    res = requests.post(URL, headers=headers, data=json.dumps(body))
    approval_key = res.json()["approval_key"]
    return approval_key

def stockspurchase_overseas(data):
    pValue = data.split('^')
    korean_date = pValue[6]
    korean_time = pValue[7]
    current_price = pValue[11]
    
    print(f"한국일자: {korean_date}")
    print(f"한국시간: {korean_time}")
    print(f"현재가: {current_price}")
    print("--------------------")

# 기존 해외주식체결처리 출력라이브러리
# def stockspurchase_overseas(data_cnt, data):
#     print("============================================")
#     menulist = "실시간종목코드|종목코드|수수점자리수|현지영업일자|현지일자|현지시간|한국일자|한국시간|시가|고가|저가|현재가|대비구분|전일대비|등락율|매수호가|매도호가|매수잔량|매도잔량|체결량|거래량|거래대금|매도체결량|매수체결량|체결강도|시장구분"
#     menustr = menulist.split('|')
#     pValue = data.split('^')
#     i = 0
#     for cnt in range(data_cnt):  # 넘겨받은 체결데이터 개수만큼 print 한다
#         print("### [%d / %d]" % (cnt + 1, data_cnt))
#         for menu in menustr:
#             print("%-13s[%s]" % (menu, pValue[i]))
#             i += 1

async def connect():
    try:
        g_appkey = "PSOMMGj57opv4saDiBelSp9usar9LtXfuko2"
        g_appsecret = "U9M/qgAs2UMY24ZIzUnTAXsXVbEROIg7Sf9cHzJyAyqJRG2e1Aen93zC55X//tCHOMXcG13Mp9Kv1+laKCpKpm+sGo9htc7/dBxiwfCOufhr8R2iI0YW512W8ESiDU3AtFRYZnq9VcvEkMggYFCKhiyuZJGt61rxzGPjg1ixondJ52KwGRU="

        url = 'ws://ops.koreainvestment.com:21000'

        g_approval_key = get_approval(g_appkey, g_appsecret)
        print("approval_key [%s]" % (g_approval_key))

        code_list = [['1','HDFSCNT0','DNASAAPL']]

        senddata_list = []
        
        for i,j,k in code_list:
            temp = '{"header":{"approval_key": "%s","custtype":"P","tr_type":"%s","content-type":"utf-8"},"body":{"input":{"tr_id":"%s","tr_key":"%s"}}}'%(g_approval_key,i,j,k)
            senddata_list.append(temp)

        async with websockets.connect(url, ping_interval=None) as websocket:
            for senddata in senddata_list:
                await websocket.send(senddata)
                await asyncio.sleep(3)
                print(f"Input Command is :{senddata}")

            while True:
                data = await websocket.recv()

                if data[0] == '0':
                    recvstr = data.split('|')
                    trid0 = recvstr[1]

                    if trid0 == "HDFSCNT0":
                        stockspurchase_overseas(recvstr[3])
                        await asyncio.sleep(3)

    except Exception as e:
        print('Exception Raised!')
        print(e)
        print('Connect Again!')
        time.sleep(0.1)
        await connect()

async def main():
    try:
        await connect()
    except Exception as e:
        print('Exception Raised!')
        print(e)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("KeyboardInterrupt Exception 발생!")
    except Exception:
        print("Exception 발생!")