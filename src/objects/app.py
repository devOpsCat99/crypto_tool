import streamlit as st
from objects.crypto import crypto
from objects.crypto_configuration import cryptoConfiguration
from objects.model_configuration import modelConfiguration

class App():
    
    def __init__(self):
        self.__coins = ["Bitcoin", "Ethereum", "Kaspa", "Ripple", "Solana", "Hyperliquid", "Raydium"]
        self.__time_periods = ["1", "2", "5", "7", "30", "90", "180", "365"]
        
        # Initialise 
        self.__selected_coin = []
        self.__selected_time_period = []
    
    # Getters
    def getCoins(self):
        return self.__coins
    
    def getTimePeriods(self):
        return self.__time_periods
    
    def getSelectedCoin(self):
        return self.__selected_coin
    
    def getSelectedTimePeriod(self):
        return self.__selected_time_period
    
    # Public methods
    def writeTitle(self, title):
        st.title(title)
        
    def writeText(self, text):
        st.write(text)
    
    def createConfig(self):
        col1, col2 = st.columns(2)
        with col1:
            selected_coin = st.selectbox("Coin:", self.__coins, index=2)
        with col2:
            selected_time_period = st.selectbox("Time period (days):", self.__time_periods, index=2)
            
        st.write(f"Your fitting configuration: {selected_coin} with a time period of {selected_time_period}.")
        
        self.__selected_coin        = selected_coin
        self.__selected_time_period = selected_time_period
        
    def createCrypto(self):
        try:
            currentValue, rentability, __, __, figureCrypto, success = crypto(cryptoConfiguration((self.__selected_coin).lower(), self.__selected_time_period), modelConfiguration()).executeAll(False) 
            st.plotly_chart(figureCrypto)
        except:
            st.write("Data unavailable.")
        
    def executeApp(self):
        self.writeTitle("Crypto Fitting Tool App") 
        self.writeText("Select the desired coin and the time period to fit the trend.")
        self.createConfig()
        self.createCrypto()
    # Private methods
    
    
    # Print
    def __str__(self):
        return "App class"