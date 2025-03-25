class modelConfiguration():
    # Constructor
    def __init__(self, fitModel = "fourier4", minLocalDiff = 0.75, thresholdAction = 3, rollingWindowFactor = 5):
        self.__fitModel            = fitModel
        self.__minLocalDiff        = minLocalDiff
        self.__thresholdAction     = thresholdAction
        self.__rollingWindowFactor = rollingWindowFactor
    
    # Setters
    def set_fitModel(self, fitModel):
        self.__fitModel = fitModel  
    
    def set_minLocalDiff(self, minLocalDiff):
        self.__minLocalDiff = minLocalDiff
    
    def set_thresholdAction(self, thresholdAction):
        self.__thresholdAction = thresholdAction
        
    def set_rollingWindowFactor(self, rollingWindowFactor): 
        self.__rollingWindowFactor = rollingWindowFactor
        

    # Getters
    def get_fitModel(self):
        return self.__fitModel  
    
    def get_minLocalDiff(self):
        return self.__minLocalDiff
    
    def get_thresholdAction(self):
        return self.__thresholdAction
    
    def get_rollingWindowFactor(self):
        return self.__rollingWindowFactor
    
    # String representation    
    def __str__(self):
        return f"Model: {self.__fitModel}, Min Local Diff: {self.__minLocalDiff}, Threshold Action: {self.__thresholdAction}, Rolling Window Factor: {self.__rollingWindowFactor}"