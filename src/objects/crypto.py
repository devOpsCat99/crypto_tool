import requests
import numpy                       as np
import pandas                      as pd
import utils.functions             as functions
import matplotlib.pyplot           as plt
import matplotlib.dates            as mdates
import plotly.graph_objects        as go
from   objects.trendMaxMinInfo     import trendMaxMinInfo
from   objects.trendReferenceLimit import trendReferenceLimit



class crypto():
    def __init__(self, cryptoCnf, modelCnf):
        self.__cryptoCnf = cryptoCnf
        self.__modelCnf  = modelCnf
        self.__name      =  self.__cryptoCnf.get_cryptoName()
        
        # inicialised as empty
        self.__prices         = []
        self.__times          = []
        self.__timesDecYear   = []
        self.__fittedPrices   = []
        self.__trendInfo      = trendMaxMinInfo()
        self.__trendReference = trendReferenceLimit()
        self.__figureCrypto   = []
        
        # load data
        self.__load_data()

    # Setters
    def set_cryptoCnf(self, cryptoCnf):
        self.__cryptoCnf = cryptoCnf
        self.__load_data()
    
    def set_modelCnf(self, modelCnf):
        self.__modelCnf = modelCnf
    
    def set_name(self, name):
        self.__name = name
        
    # Getters
    def get_cryptoCnf(self):
        return self.__cryptoCnf
    
    def get_modelCnf(self):
        return self.__modelCnf
    
    def get_name(self):
        return self.__name
    
    def get_prices(self):
        return self.__prices
    
    def get_times(self):
        return self.__times
    
    def get_timesDecYear(self):
        return self.__timesDecYear
    
    def get_fittedPrices(self):
        return self.__fittedPrices
    
    def get_trendInfo(self):
        return self.__trendInfo
    
    def get_trendReference(self):
        return self.__trendReference
    
    def get_figureCrypto(self):
        return self.__figureCrypto
    
    # public methods
    def executeFitData(self):
        self.__fitData()
        
    def executeFindMaxMin(self):
        self.__findMaxMin()
    
    def executeLimitReference(self):
        self.__limitReference(len(self.__trendInfo.get_localIdxs()))
        
    def executePlotting(self, plotFlag):
        #return self.__plotting(plotFlag)
        return  self.__plotting_interactive(plotFlag)
        
    def executeAll(self, plotFlag = False):
        try:
            self.executeFitData()
            self.executeFindMaxMin()
            self.executeLimitReference()
            self.__figureCrypto = self.executePlotting(plotFlag)
            return self.__prices[-1], self.__trendReference.get_refImprovement(), pd.DataFrame({"time": self.__times, "price": self.__prices, "fittedPrice": self.__fittedPrices}), self.__trendReference, self.__figureCrypto, True
        except:
            return [], [], [], [], [], False       
        
    # private methods
    def __load_data(self):
        data                = pd.DataFrame(((requests.get(self.__cryptoCnf.get_full_url(), verify=True)).json()) ["prices"], columns=['timestamp', 'price'])
        self.__prices       = data['price'].values
        self.__times        = pd.to_datetime(data['timestamp'], unit='ms', utc=True)
        self.__timesDecYear = functions.pdTime_to_decYear(self.__times)
     
    def __fitData(self):
        self.__fittedPrices = (pd.Series(functions.fit_data(self.__timesDecYear, self.__prices, np.ones(10), self.__modelCnf.get_fitModel())).rolling(window = self.__modelCnf.get_rollingWindowFactor(), center=True, min_periods=1).mean()).values
    
    def __findMaxMin(self):
        self.__trendInfo.set_localIdxs(functions.find_local_max_min(self.__fittedPrices))
        self.__trendInfo.set_localPrices(self.__fittedPrices[self.__trendInfo.get_localIdxs()])
        self.__trendInfo.set_localImprovement(np.hstack([100 * ((self.get_trendInfo().get_localPrices()[0] / self.__prices[0]) - 1), [100 * ((self.get_trendInfo().get_localPrices()[ii] / self.get_trendInfo().get_localPrices()[ii - 1]) - 1) for ii in range(1, len(self.get_trendInfo().get_localPrices()))]]))
    
    def __limitReference(self, Nlocal):
        if Nlocal < 0:
            self.__trendReference.set_refIdx(0)
            self.__trendReference.set_refPrice(self.__prices[0])
            self.__trendReference.set_currentPrice(self.__fittedPrices[-1])
            self.__trendReference.set_refImprovement(100 * (self.__trendReference.get_currentPrice() / self.__trendReference.get_refPrice() - 1))
        else:
            self.__trendReference.set_refIdx(self.__trendInfo.get_localIdxs()[Nlocal - 1])
            self.__trendReference.set_refPrice(self.__trendInfo.get_localPrices()[Nlocal - 1])
            self.__trendReference.set_currentPrice(self.__fittedPrices[-1])
            self.__trendReference.set_refImprovement(100 * (self.__trendReference.get_currentPrice() / self.__trendReference.get_refPrice() - 1))   
            
            if np.abs(self.__trendInfo.get_localImprovement()[Nlocal - 1]) < np.abs(self.__modelCnf.get_minLocalDiff()):
                self.__limitReference(Nlocal - 2)      
    
    def __plotting(self, plotFlag):        
        plt.style.use('seaborn-v0_8-darkgrid')
        plt.rcParams['font.family'] = 'serif'
        figure, ax = plt.subplots(figsize=(10, 6))
        ax.plot(self.__times, self.__prices, label=f"Price [{self.__cryptoCnf.get_currency()}]", 
                color='royalblue', linewidth=1.5, alpha=0.7)
        ax.plot(self.__times, self.__fittedPrices, color='crimson', linewidth=3, label="Tendencia")
        ax.axvline(x=self.__times[self.__trendReference.get_refIdx()], linestyle="--", 
                color="gray", linewidth=1, alpha=0.7)
        ax.axhline(y=self.__trendReference.get_refPrice(), linestyle="--", 
                color="gray", linewidth=1, alpha=0.7)
        ax.scatter(self.__times[self.__trendReference.get_refIdx()], self.__trendReference.get_refPrice(), 
                color='black', s=50, label="Referencia")
        ax.plot(self.__times[self.__trendReference.get_refIdx():], 
                functions.fit_data(self.__timesDecYear[self.__trendReference.get_refIdx():], 
                                self.__fittedPrices[self.__trendReference.get_refIdx():], np.ones(2), "lineal"), 
                '-', color='black', linewidth=3, alpha=0.8)
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())  
        ax.xaxis.set_major_formatter(mdates.AutoDateFormatter(ax.xaxis.get_major_locator())) 
        plt.xticks(rotation=30, fontsize=10)  # Rotar etiquetas para mejor lectura
        figure.autofmt_xdate()
        plt.yticks(fontsize=10)
        ax.set_facecolor('white')
        ax.text(self.__times.values[-1], self.__prices[-1], 
                f"{(self.__trendReference.get_refImprovement()):.2f} %", 
                fontweight='bold', fontsize=12, color="black")
        ax.set_xlim([min(self.__times), max(self.__times)])
        ax.set_ylim([min(self.__prices), max(self.__prices)])
        ax.grid(True, which='both', axis='both', color='gray', linestyle=':', linewidth=0.5)
        ax.set_ylabel(f"Price [{self.__cryptoCnf.get_currency()}]", fontsize=12)
        if plotFlag:
            figure.savefig("grafico2_mejorado.png", format="png", dpi=500, bbox_inches="tight")
            plt.show()
        
        return figure
        
    def __plotting_interactive(self, plotFlag):
        
        fig = go.Figure()

        # Línea de precios
        fig.add_trace(go.Scatter(
            x=self.__times,
            y=self.__prices,
            mode='lines',
            name=f"Price [{self.__cryptoCnf.get_currency()}]",
            line=dict(color='royalblue', width=1.5),
            hoverinfo="x+y+name"
        ))

        # Línea de tendencia
        fig.add_trace(go.Scatter(
            x=self.__times,
            y=self.__fittedPrices,
            mode='lines',
            name=f"Trend [{self.__cryptoCnf.get_currency()}]",
            line=dict(color='crimson', width=3),
            hoverinfo="x+y+name"
        ))

        # Línea vertical de referencia
        fig.add_trace(go.Scatter(
            x=[self.__times[self.__trendReference.get_refIdx()]] * 2,
            y=[min(self.__prices), max(self.__prices)],
            mode='lines',
            line=dict(color="gray", width=1, dash="dash"),
            hoverinfo="none"
        ))

        # Línea horizontal de referencia
        fig.add_trace(go.Scatter(
            x=[min(self.__times), max(self.__times)],
            y=[self.__trendReference.get_refPrice()] * 2,
            mode='lines',
            line=dict(color="gray", width=1, dash="dash"),
            hoverinfo="none"
        ))

        # Punto de referencia
        fig.add_trace(go.Scatter(
            x=[self.__times[self.__trendReference.get_refIdx()]],
            y=[self.__trendReference.get_refPrice()],
            mode='markers',
            marker=dict(color='black', size=8),
            hoverinfo="none"
        ))

        # Línea de ajuste posterior a la referencia
        fit_prices = functions.fit_data(
            self.__timesDecYear[self.__trendReference.get_refIdx():],
            self.__fittedPrices[self.__trendReference.get_refIdx():],
            np.ones(2), "lineal"
        )
        fig.add_trace(go.Scatter(
            x=self.__times[self.__trendReference.get_refIdx():],
            y=fit_prices,
            mode='lines',
            line=dict(color='black', width=3),
            hoverinfo="none"
        ))

        fig.add_annotation(
            x=self.__times.values[-1],
            y=self.__prices[-1],
            text=f"{self.__trendReference.get_refImprovement():.2f} %",
            showarrow=False,
            font=dict(size=12, color="black", family="Arial Black"),
            xref="paper",  # Fija la anotación en el espacio relativo del gráfico
            yref="paper",  # Fija la anotación en el espacio relativo del gráfico
            xanchor="left",  # Anclar la anotación hacia la izquierda
            yanchor="bottom"  # Anclar la anotación hacia abajo
        )
        
        # Configuración de diseño
        fig.update_layout(
            xaxis=dict(
                title="Time",
                showgrid=True, gridcolor="lightgray", gridwidth=0.5
            ),
            yaxis=dict(
                title=f"Price [{self.__cryptoCnf.get_currency()}]",
                showgrid=True, gridcolor="lightgray", gridwidth=0.5
            ),
            plot_bgcolor="white",
            hovermode="x",
            showlegend=False  # Oculta la leyenda
        )

        if plotFlag:
            print("SAVING PLOT")

        return fig
    
    def __str__(self):
        return f"Coin Object: {self.__name}"