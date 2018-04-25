
class IPTable:

    def __init__(self, scopeID, ipScope):
        self.scopeID = scopeID
        self.ipScope = ipScope

    def printTable(self):
        raise NotImplementedError("Subclass must implement abstract method")

    
