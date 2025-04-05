import os

class cryptoConfiguration():
    
    # Constructor
    def __init__(self, cryptoName, period, currency):
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
        self.__full_url = []

    # String representation
    def __str__(self):
        return self.get_full_url()

class cryptoConfiguration_coingecko(cryptoConfiguration):
    
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
    
class cryptoConfiguration_bitvavo(cryptoConfiguration):
    
    # Constructor
    def __init__(self, cryptoName, period = 2):
        self.__cryptoName = cryptoName
        self.__currency   = "eur" # USD does not exist in Bitvavo
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

    def get_acronym(self):
        return self.__cryptoAcronym
    
    def get_interval(self):
        return self.__cryptoInterval
    
    def get_samples(self):
        return self.__cryptoSamples
    
    def get_full_url(self):
        return self.__full_url
    
    # Private method
    def __create_full_url(self):
        self.__cryptoAcronym = self.__get_acronym(self.__cryptoName)
        self.__cryptoInterval = self.__get_interval(self.__period)
        self.__cryptoSamples = self.__calculate_samples(self.__cryptoInterval, self.__period)
        self.__full_url = f"https://api.bitvavo.com/v2/{self.__cryptoAcronym}-{self.__currency.upper()}/candles?interval={self.__cryptoInterval}&limit={self.__cryptoSamples}"

    def __get_acronym(self, cryptoName):
        mapping = {
            "bitcoin":     "BTC",
            "ethereum":    "ETH",
            "kaspa":       "KAS",
            "ripple":      "XRP",
            "solana":      "SOL",
            "hyperliquid": "HYPE",
            "raydium":     "RAY",
        }
        return mapping.get(cryptoName.lower(), None).upper()
    
    def __get_interval(self, period):
        periods = {
            '1':   "5m",
            '2':   "1h",
            '5':   "1h",
            '7':   "1h",
            '30':  "1h",
            '90':  "2h",
            '180': "1d",
            '365': "1d",
        }
        return periods.get(period, "1h")
    def __calculate_samples(self, interval, period):
        intervals = {
            "5m":  288,
            "1h":  24,
            "1d":  1,
            "2h":  12,
        }
        return intervals.get(interval, 0) * float(period)   
       
    # String representation
    def __str__(self):
        return self.get_full_url()