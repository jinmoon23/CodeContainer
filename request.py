import websockets
import json
import asyncio

STOCK_CODE = "005930"  # 삼성전자 종목코드
current_price = None

async def connect_and_subscribe():
    url = "ws://localhost:8765"  # 모의 서버 주소
    async with websockets.connect(url) as websocket:
        while True:
            try:
                data = await websocket.recv()
                print("Received data:", data)  # 디버깅을 위해 원시 데이터 출력
                json_data = json.loads(data)
                
                if json_data["type"] == "0":  # 실시간 데이터
                    recvstr = json_data["data"].split('|')
                    if recvstr[0] == "H0STCNT0":  # 주식체결 데이터
                        trade_data = recvstr[2].split('^')
                        current_price = float(trade_data[0])  # 현재가 추출 및 저장
                        print("실시간 체결 데이터:")
                        print(f"종목코드: {recvstr[1]}")
                        print(f"현재가: {current_price}")
                        print(f"거래량: {trade_data[1]}")
                        print(f"전일대비구분: {trade_data[2]}")
                        print(f"전일대비: {trade_data[3]}")
                        print(f"등락율: {trade_data[4]}")
                        print("---")
                        await process_price(current_price)
                else:
                    print("기타 메시지:", data)
            except websockets.exceptions.ConnectionClosed:
                print("WebSocket 연결이 종료되었습니다.")
                break
            except json.JSONDecodeError:
                print("잘못된 JSON 형식:", data)
            except Exception as e:
                print(f"오류 발생: {e}")
                print(f"데이터: {data}")  # 오류 발생 시 원본 데이터 출력

async def process_price(price):
    """가격 정보를 활용하는 함수"""
    print(f"현재 가격: {price}원")
    # 여기에 가격 정보를 활용하는 로직을 추가할 수 있습니다.
    # 예: 데이터베이스에 저장, 알림 발송, 차트 업데이트 등

asyncio.get_event_loop().run_until_complete(connect_and_subscribe())