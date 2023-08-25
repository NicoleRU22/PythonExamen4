import requests

def get_bitcoin_precio():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  
        data = response.json()
        return float(data["bpi"]["USD"]["rate"].replace(",", ""))
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def calcular(bitcoins, price):
    return bitcoins * price

def main():
    try:
        n = input("Ingresar la cantidad de bitcoins que tiene: ")
        
        bitcoin_precio = get_bitcoin_precio()
        if bitcoin_precio is not None:
            costo_usd = calcular(n, bitcoin_precio)
            formatear = "{:,.3f}".format(costo_usd)
            print(f"El costo de {n} Bitcoins es ${formatear} USD.")
    except ValueError:
        print("Error")

if __name__ == "__main__":
    main()
