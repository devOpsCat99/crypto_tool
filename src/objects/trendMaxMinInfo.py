class trendMaxMinInfo:
    def __init__(self):
        self.__localIdxs        = []
        self.__localPrices      = []
        self.__localImprovement = []

    # Setters
    def set_localIdxs(self, localIdxs):
        self.__localIdxs = localIdxs
    
    def set_localPrices(self, localPrices):
        self.__localPrices = localPrices
        
    def set_localImprovement(self, localImprovement):
        self.__localImprovement = localImprovement  
        
    # Getters
    def get_localIdxs(self):
        return self.__localIdxs
    
    def get_localPrices(self):
        return self.__localPrices
    
    def get_localImprovement(self):
        return self.__localImprovement
    
    # Print
    def __str__(self):
        return "localIdxs: " + str(self.__localIdxs) + "\n" + "localPrices: " + str(self.__localPrices) + "\n" + "localImprovement: " + str(self.__localImprovement) + "\n"       