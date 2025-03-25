from objects.crypto_configuration import cryptoConfiguration
from objects.model_configuration  import modelConfiguration
from objects.crypto               import crypto

def main():
    print("Ejecutando el proyecto...")
    currentValue, rentability, data, success = crypto(cryptoConfiguration("bitcoin",2), modelConfiguration()).executeAll(True) 
    print("Valor actual: ", currentValue)
    print("Rentabilidad: ", rentability)  
     
if __name__ == "__main__":
    main()