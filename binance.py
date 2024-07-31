from binance.client import Client
from binance.exceptions import BinanceAPIException
import os

# Configura tus claves API aquí
API_KEY = 'tu_api_key'
API_SECRET = 'tu_api_secret'

# Crea una instancia del cliente de Binance
client = Client(API_KEY, API_SECRET)

def obtener_saldo_futuros_usdt():
    try:
        # Conéctate al cliente de futuros
        futures_client = client.futures_account()
        
        # Obtén el saldo en futuros
        saldo = futures_client['totalWalletBalance']
        print(f"Saldo total disponible en futuros: {saldo} USDT")
        
    except BinanceAPIException as e:
        print(f"Error en la conexión con Binance API: {e}")

if __name__ == "__main__":
    obtener_saldo_futuros_usdt()
