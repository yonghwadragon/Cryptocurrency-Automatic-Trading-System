import os
from dotenv import load_dotenv   #pip install python-dotenv
load_dotenv()
import google.generativeai as genai #pip install -q -U google-generativeai
import pyupbit #pip install pyupbit
import json

# Setup
client = genai(api_key=os.getenv("Gemini_api_key"))
upbit = pyupbit.Upbit(os.getenv("upbit_api_Access_key"), os.getenv("upbit_api_Secret_key"))

def get_current_status():
    orderbook = pyupbit.get_orderbook(ticker="KRW-BTC") #get_orderbook는 매수/매도 호가 정보를 조회합니다.
    current_time = orderbook['timestamp'] #현재 시간
    btc_balance = 0 #비트코인 잔고 = 0
    krw_balance = 0 #원화의 현재 잔액=  0
    btc_avg_buy_price = 0 #비트코인의 평균 매수 가격 = 0
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == "BTC":
            btc_balance = b['balance']
            btc_avg_buy_price = b['avg_buy_price']
        if b['currency'] == "KRW":
            krw_balance = b['balance']

    current_status = {'current_time': current_time, 'orderbook': orderbook, 'btc_balance': btc_balance, 'krw_balance': krw_balance, 'btc_avg_buy_price': btc_avg_buy_price}
    return json.dumps(current_status)