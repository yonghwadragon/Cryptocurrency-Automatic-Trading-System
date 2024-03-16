import os
from dotenv import load_dotenv   
load_dotenv()
import google.generativeai as genai 
import pyupbit 
import json

# Setup
client = genai.configure(api_key=os.getenv("Gemini_api_key"))
upbit = pyupbit.Upbit(
    os.getenv("upbit_api_Access_key"),
    os.getenv("upbit_api_Secret_key")
)

def get_current_status(): 
    orderbook = pyupbit.get_orderbook(ticker="KRW-BTC")
    current_time = orderbook['timestamp'] 
    btc_balance = 0  
    krw_balance = 0 
    btc_avg_buy_price = 0 
    balances = upbit.get_balances()
    for b in balances:     
        if b['currency'] == "BTC":  
            btc_balance = b['balance'] 
            btc_avg_buy_price = b['avg_buy_price'] 
        if b['currency'] == "KRW": 
            krw_balance = b['balance'] 

    current_status = {
    'current_time': current_time,
    'orderbook': orderbook,
    'btc_balance': btc_balance,
    'krw_balance': krw_balance,
    'btc_avg_buy_price': btc_avg_buy_price} 
    return json.dumps(current_status)