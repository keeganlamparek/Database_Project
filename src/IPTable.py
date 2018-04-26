
class IPTable:

    def __init__(self, scopeID):
        self.scopeID = scopeID

    def printTable(self):
        raise NotImplementedError("Subclass must implement abstract method")

    
