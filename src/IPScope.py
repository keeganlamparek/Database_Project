from DataConnection import DataConnection

class IPScope:

    ipScopeTable = "IPScope"
    scopeIDColumn = "ScopeID"
    ipScopeColumn = "IPScope"
    cityIDColumn = "CityID"

    def __init__(self, scopeID):
        self.scopeID = scopeID
        

    @classmethod
    def returnAddresses(self, scopeID):
        addresses = self.selectQuery(self, self.ipScopeColumn, self.scopeIDColumn, scopeID)
        return addresses

    def selectQuery(self, selectStatement, whereColumn, attributeValue):
        connection = DataConnection()

        query = "SELECT " + selectStatement + " FROM " + self.ipScopeTable + " WHERE " + whereColumn + " = " + attributeValue

        connection.runQuery(query)