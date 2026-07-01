import os
from binance.client import Client
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")
client = Client(api_key, api_secret, testnet=True)

try:
    info = client.futures_exchange_info()
    symbols = info['symbols']
    btc_info = next((s for s in symbols if s['symbol'] == 'BTCUSDT'), None)
    if btc_info:
        print("BTCUSDT Order Types:", btc_info['orderTypes'])
except Exception as e:
    print("Error:", e)
