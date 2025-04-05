from objects.crypto_configuration import cryptoConfiguration, cryptoConfiguration_coingecko, cryptoConfiguration_bitvavo
from objects.model_configuration  import modelConfiguration
from objects.crypto               import crypto

def main():
    print("Ejecutando el proyecto...")
    crypto(cryptoConfiguration_bitvavo("raydium",5), modelConfiguration()).executeAll(False) 
     
if __name__ == "__main__":
    main()