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

def handle_binance():
    print("Configurando Binance...")
    # el codigo para cada exchange

def handle_bybit():
    print("Configurando Bybit...")
    # el codigo para cada exchange

def handle_bitget():
    print("Configurando Bitget...")
    # el codigo para cada exchange

def main():
    selected_exchange = select_exchange()
    print(f"Has seleccionado: {selected_exchange}")

    if selected_exchange == 'Binance':
        handle_binance()
    elif selected_exchange == 'Bybit':
        handle_bybit()
    elif selected_exchange == 'Bitget':
        handle_bitget()

if __name__ == "__main__":
    main()
