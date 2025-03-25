class trendReferenceLimit:
    def __init__(self):
        self.__refIdx         = []
        self.__refPrice       = []
        self.__currentPrice   = []
        self.__refImprovement = []


    # Setters
    def set_refIdx(self, refIdx):
        self.__refIdx = refIdx
        
    def set_refPrice(self, refPrice):
        self.__refPrice = refPrice
        
    def set_currentPrice(self, currentPrice):
        self.__currentPrice = currentPrice
        
    def set_refImprovement(self, refImprovement):
        self.__refImprovement = refImprovement
        
    # Getters
    def get_refIdx(self):
        return self.__refIdx
    
    def get_refPrice(self):
        return self.__refPrice
    
    def get_currentPrice(self):
        return self.__currentPrice
    
    def get_refImprovement(self):
        return self.__refImprovement
    
    # Private methods
    def __str__(self):
        return str(self.__dict__)