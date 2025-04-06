class Action():
    
    # Constructor
    def __init__(self, price):
        self.__price = price
        
    # Getters
    def getPrice(self):
        return self.__price
    
    # Public Methods
    def execute(self):
        pass
    
    def prova(self):
        print("prova")
        
    # Print
    def __str__(self):
        return "Price: " + str(self.__price)
