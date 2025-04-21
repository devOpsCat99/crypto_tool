import streamlit as st
from objects.crypto import crypto
from objects.crypto_configuration import cryptoConfiguration_coingecko, cryptoConfiguration_bitvavo
from objects.model_configuration import modelConfiguration

class App():
    
    def __init__(self):
        self.__coins = ["Bitcoin", "Ethereum", "Kaspa", "Ripple", "Solana", "Hyperliquid", "Raydium"]
        self.__time_periods = ["1", "2", "5", "7", "30", "90", "180", "365"]
        
        # Initialise 
        self.__selected_coin = []
        self.__selected_time_period = []
        self.__interactive_plot = []
        self.__currency = []
        
    # Getters
    def getCoins(self):
        return self.__coins
    
    def getTimePeriods(self):
        return self.__time_periods
    
    def getSelectedCoin(self):
        return self.__selected_coin
    
    def getSelectedTimePeriod(self):
        return self.__selected_time_period
    
    def getInteractivePlot(self):
        return self.__interactive_plot
    
    def getCurrency(self):
        return self.__currency
    
    def getApi(self):
        return self.__api
    
    # Public methods
    def writeTitle(self, title):
        st.title(title)
        
    def writeText(self, text):
        st.write(text)            
                    
    def createCoinSelector(self):
        self.__selected_coin = st.selectbox("Coin:", self.__coins, index=2)
        
    def createTimePeriodSelector(self):
        self.__selected_time_period = st.radio("Time period (days):", options=self.__time_periods, index = 2, horizontal = True)
    
    def createPlotSelector(self):
        self.__interactive_plot = False
         
    def createCurrencySelector(self):
        if "currency" not in st.session_state:
            st.session_state.currency = "eur"

        if st.button("€" if st.session_state.currency == "usd" else "$"): # inverted symbols as it represents future currency to select
            st.session_state.currency = "eur" if st.session_state.currency == "usd" else "usd"
            st.rerun() # since button updates before currency by streamlit functionality
        
        self.__currency = st.session_state.currency

    def createApiSelector(self):
        if "api" not in st.session_state:
            st.session_state.api = "Bitvavo"

        if st.button("Bitvavo" if st.session_state.api == "Coingecko" else "Coingecko"): # inverted symbols as it represents future API to select
            st.session_state.api = "Bitvavo" if st.session_state.api == "Coingecko" else "Coingecko"
            st.rerun() # since button updates before api by streamlit functionality
        
        self.__api = st.session_state.api

    def createConfig(self):
        col1, col2 = st.columns([1, 4.5])
        with col1:
            self.createCoinSelector()
        with col2:
            self.createTimePeriodSelector()
        col3, col4 = st.columns([1, 15])
        with col3:
            self.createCurrencySelector()
        with col4:
            self.createApiSelector()   
        self.createPlotSelector()
        
    def createCrypto(self):
        try:
            if self.__api == "Coingecko":
                currentValue, rentability, __, __, figureCrypto, success = crypto(cryptoConfiguration_coingecko((self.__selected_coin).lower(), self.__selected_time_period, currency = self.__currency), modelConfiguration()).executeAll(self.__interactive_plot) 
            
            elif self.__api == "Bitvavo":            
                if self.__currency == "usd":
                    st.session_state.currency = "eur"
                    self.__currency = st.session_state.currency
                    st.rerun() # since button updates before currency by streamlit functionality
                self.writeText("Bitvavo API only supports EUR currency.")
                currentValue, rentability, __, __, figureCrypto, success = crypto(cryptoConfiguration_bitvavo((self.__selected_coin).lower(), self.__selected_time_period), modelConfiguration()).executeAll(self.__interactive_plot) 
            
            colAPI, colPlotting, __ = st.columns([1.4, 1.4, 1.4])
            with colAPI:
                st.markdown(f"###### {self.__api}: {self.__selected_coin}({self.__currency})")
            with colPlotting:
                st.markdown(f"###### +{currentValue:.4f} {self.__currency} ({rentability:.2f} %)")
            
            if not self.__interactive_plot:
                st.pyplot(figureCrypto, use_container_width=True)
            elif self.__interactive_plot:
                st.plotly_chart(figureCrypto, use_container_width=True)
        except Exception as e:
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