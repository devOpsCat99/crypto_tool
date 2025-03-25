import os

class cryptoConfiguration:
    # Constructor
    def __init__(self, cryptoName, period = 2, currency = "usd"):
        self.__cryptoName = cryptoName
        self.__currency   = currency
        self.__period     = period
        self.__create_full_url()

    # Setters
    def set_cryptoName(self, cryptoName):
        self.__cryptoName = cryptoName
        self.__create_full_url()

    def set_currency(self, currency):
        self.__currency = currency
        self.__create_full_url()

    def set_period(self, period):
        self.__period = period
        self.__create_full_url()    

    # Getters
    def get_cryptoName(self):
        return self.__cryptoName
    
    def get_currency(self): 
        return self.__currency
    
    def get_period(self):
        return self.__period    

    def get_full_url(self):
        return self.__full_url
    
    # Private method
    def __create_full_url(self):
        self.__full_url = f"https://api.coingecko.com/api/v3/coins{os.sep}{self.__cryptoName}{os.sep}market_chart?vs_currency={self.__currency}&days={self.__period}"

    # String representation
    def __str__(self):
        return self.get_full_url()