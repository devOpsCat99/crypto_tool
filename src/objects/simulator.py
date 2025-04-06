from objects.buy  import Buy
from objects.sell import Sell
from objects.file import File
from objects.crypto   import crypto

import time

class Simulator():
    
    # Constructor
    def __init__(self, cryptoCnf, modelCnf, filePath, startingMoney, marketAction = 3):
        self.__cryptoCnf     = cryptoCnf
        self.__modelCnf      = modelCnf
        self.__filePath      = filePath
        self.__startingMoney = startingMoney
        self.__marketAction  = marketAction
        
        # Initialise
        self.__CoinName          = self.__cryptoCnf.get_cryptoName()
           
        self.__startingPrice, __, __, __, __, __ = crypto(self.__cryptoCnf, self.__modelCnf).executeAll(False)
        
        self.__currentAction     = Buy(self.__startingPrice, self.__startingMoney)
        self.__startingCoins     = self.__executeBuy()
        
        self.__coins             = self.__startingCoins
        self.__money             = 0 # as buy action has been done
        self.__price             = self.__startingPrice
        
        self.__file              = File(self.__filePath)
        self.__createFile()
        
        self.__instantRent          = 0
        self.__accumulatedRent      = 0
        self.__accumulatedCoinsRent = 0

    # Getters
    def getCoins(self):
        return self.__coins
    
    def getPrice(self):
        return self.__price
    
    def getMoney(self):
        return self.__money
    
    def getAction(self):
        return self.__currentAction
    
    def getFile(self):
        return self.__file
    
    def getCoinName(self):
        return self.__CoinName
    
    def getCryptoCnf(self):
        return self.__cryptoCnf
    
    def getModelCnf(self):
        return self.__modelCnf
    
    def getStartingPrice(self):
        return self.__startingPrice
    
    def getStartingMoney(self):
        return self.__startingMoney
    
    def getStartingCoins(self):
        return self.__startingCoins
    
    def getInstantRent(self):
        return self.__instantRent
    
    def getAccumulatedRent(self):
        return self.__accumulatedRent
    
    def getAccumulatedCoinsRent(self):
        return self.__accumulatedCoinsRent
    
    def getMarketAction(self):
        return self.__marketAction
    
    # Public Methods            
    def run(self):
        while True:
            time.sleep(300)
            print("NeW Iteration")
            try:
                currentPriceCoin, marketStatus, __, __, __, __ = crypto(self.__cryptoCnf, self.__modelCnf).executeAll(False)
                if  not (self.__coins == 0) and marketStatus <= - self.__marketAction:
                    self.__sellFunction(currentPriceCoin, marketStatus)
                    
                if not (self.__money == 0) and marketStatus >= self.__marketAction:
                    self.__buyFunction(currentPriceCoin, marketStatus)
            except:
                pass

    # Private methods
    def __sellFunction(self, priceCoin, marketStatus):
        if  not (self.__coins == 0) and marketStatus <= - self.__marketAction:
            self.__instantRent = ((Sell(priceCoin, self.__coins).execute() / self.__currentAction.getMoney()) - 1) * 100
            self.__accumulatedRent = ((Sell(priceCoin, self.__coins).execute() / self.__startingMoney) - 1) * 100
            self.__accumulatedCoinsRent = ((self.__coins / self.__startingCoins) - 1) * 100
            
            self.__currentAction = Sell(priceCoin, self.__coins)
            self.__coins = 0 # as sell action has been done
            self.__money = self.__executeSell()
            self.__price = priceCoin
            self.__writeSell(marketStatus)
    
    def __buyFunction(self, priceCoin, marketStatus):
        if not (self.__money == 0) and marketStatus >= self.__marketAction:
            self.__instantRent = ((Buy(priceCoin, self.__money).execute() / self.__currentAction.getCoins()) - 1) * 100
            self.__accumulatedRent = ((self.__money / self.__startingMoney) - 1) * 100
            self.__accumulatedCoinsRent = ((Buy(priceCoin, self.__money).execute() / self.__startingCoins) - 1) * 100       
            
            self.__currentAction = Buy(priceCoin, self.__money)
            self.__coins = self.__executeBuy()
            self.__money = 0 # as buy action has been done
            self.__price = priceCoin
            self.__writeBuy(marketStatus)
    
    def __executeSell(self):
        return self.__currentAction.execute()
    
    def __executeBuy(self):
        return self.__currentAction.execute()
    
    def __createFile(self):
        self.__file.createFile(self.__CoinName, self.__startingPrice, self.__startingMoney, self.__startingCoins, self.__cryptoCnf.get_currency())
    
    def __writeSell(self, marketStatus):
        self.__file.writeToFileSell(self.__CoinName, self.__price, self.__currentAction.getCoins(), self.__money, self.__instantRent, self.__accumulatedRent, self.__accumulatedCoinsRent, self.__cryptoCnf.get_currency(), marketStatus)
    
    def __writeBuy(self, marketStatus):
        self.__file.writeToFileBuy(self.__CoinName, self.__price, self.__currentAction.getMoney(), self.__coins, self.__instantRent, self.__accumulatedRent, self.__accumulatedCoinsRent, self.__cryptoCnf.get_currency(), marketStatus)
    
    # Print
    def __str__(self):
        return " Coins: " + str(self.__Coins) + " Price: " + str(self.__Price) + " Money: " + str(self.__Money)
    

    

