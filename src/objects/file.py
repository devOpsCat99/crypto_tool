from datetime import datetime
class File():
    
    # Constructor
    def __init__(self, filePath):
        self.__filePath = filePath
        
    # Getters
    def getFilePath(self):
        return self.__filePath

    # Public Methods
    def createFile(self, coinName, startingPrice, startingMoney, startingCoins, currency):
        with open(self.__filePath, 'w') as f:
            f.write(f"Coin: {coinName} | Start Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("       Date             Action     Price        Trend        Input              Output           Inst. %    Acc. Money %  Acc. Coin %\n")
            f.write(" ------------------------------------------------------------------------------------------------------------------------------------\n")
            f.write(f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}     {'Buy'.ljust(4)}     {str(f'{startingPrice:.{4}f}').ljust(8)}     {str(f'0').ljust(6)}{('%').ljust(2)}     {str(f'{startingMoney:.{3}f}').ljust(8)} {currency.ljust(6)}     {str(f'{startingCoins:.{3}f}').ljust(8)} {str(coinName).ljust(6)}     {str(0).ljust(8)}     {str(0).ljust(8)}     {str(0).ljust(8)}\n")
        f.close()
    
    def writeToFileSell(self, coinName, price, coins, money, instantRent, accumulatedRent, accumulatedCoin, currency, marketStatus):
        with open(self.__filePath, 'a') as f:
            f.write(f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}     {'Sell'.ljust(4)}     {str(f'{price:.{4}f}').ljust(8)}     {str(f'{marketStatus:.{2}f}').ljust(6)}{('%').ljust(2)}     {str(f'{coins:.{3}f}').ljust(8)} {str(coinName).ljust(6)}     {str(f'{money:.{3}f}').ljust(8)} {currency.ljust(6)}     {str(f'{instantRent:.{3}f}').ljust(8)}     {str(f'{accumulatedRent:.{3}f}').ljust(8)}     {str(f'{accumulatedCoin:.{3}f}').ljust(8)}\n")
        f.close()
    
    def writeToFileBuy(self, coinName, price, money, coins, instantRent, accumulatedRent, accumulatedCoin, currency, marketStatus):
        with open(self.__filePath, 'a') as f:
            f.write(f" {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}     {'Buy'.ljust(4)}     {str(f'{price:.{4}f}').ljust(8)}     {str(f'{marketStatus:.{2}f}').ljust(6)}{('%').ljust(2)}     {str(f'{money:.{3}f}').ljust(8)} {currency.ljust(6)}     {str(f'{coins:.{3}f}').ljust(8)} {str(coinName).ljust(6)}     {str(f'{instantRent:.{3}f}').ljust(8)}     {str(f'{accumulatedRent:.{3}f}').ljust(8)}     {str(f'{accumulatedCoin:.{3}f}').ljust(8)}\n")
        f.close()
        
    # Print
    def __str__(self):
        return " File Path: " + str(self.__filePath)