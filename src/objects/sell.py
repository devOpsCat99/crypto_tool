from objects.action import Action
class Sell(Action):
    
    # Constructor
    def __init__(self, sellPrice, coins):
        self.__sellPrice = sellPrice
        self.__Coins = coins
        
    # Getters  
    def getSellPrice(self):
        return self.__sellPrice
    def getCoins(self):
        return self.__Coins
    
    # Private Methods
    def execute(self):
        return self.__sellPrice * self.__Coins
    
    # Print
    def __str__(self):
        return "Sell Price: " + str(self.__sellPrice) + " Coins: " + str(self.__Coins)