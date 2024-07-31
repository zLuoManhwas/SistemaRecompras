import subprocess

def select_exchange():
    print("Selecciona el exchange que quieres usar:")
    print("1. Binance")
    print("2. Bybit")
    print("3. Bitget")

    choice = input("Introduce el numero de la opcion (1/2/3): ")

    if choice == '1':
        exchange = 'Binance'
    elif choice == '2':
        exchange = 'Bybit'
    elif choice == '3':
        exchange = 'Bitget'
    else:
        print("Opcion no valida. Por favor, elige 1, 2 o 3.")
        return select_exchange()

    return exchange

def main():
    selected_exchange = select_exchange()
    print(f"Has seleccionado: {selected_exchange}")

    if selected_exchange == 'Binance':
        subprocess.run(['python', 'binance.py'])
    elif selected_exchange == 'Bybit':
        subprocess.run(['python', 'bybit.py'])
    elif selected_exchange == 'Bitget':
        subprocess.run(['python', 'bitget.py'])

if __name__ == "__main__":
    main()
