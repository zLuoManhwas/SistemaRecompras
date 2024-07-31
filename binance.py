from binance.client import Client
from binance.exceptions import BinanceAPIException
import os

# Configura tus claves API aca
API_KEY = 'tu_api_key'
API_SECRET = 'tu_api_secret'

client = Client(API_KEY, API_SECRET)

def obtener_saldo_futuros_usdt():
    try:
        # Conctate al cliente de futuros
        futures_client = client.futures_account()
        
        # Obten el saldo en futuros
        saldo = futures_client['totalWalletBalance']
        print(f"Saldo total disponible en futuros: {saldo} USDT")
        
    except BinanceAPIException as e:
        print(f"Error en la conexion con Binance API: {e}")

if __name__ == "__main__":
    obtener_saldo_futuros_usdt()
