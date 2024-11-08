import asyncio
import websockets
import json
import random

async def mock_stock_data(websocket, path):
    while True:
        mock_data = {
            "type": "0",
            "data": f"H0STCNT0|005930|{random.randint(60000, 70000)}^{random.randint(1000000, 2000000)}^1^100^0.15"
        }
        await websocket.send(json.dumps(mock_data))
        await asyncio.sleep(1)  # 1초마다 데이터 전송

start_server = websockets.serve(mock_stock_data, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()