from DataConnection import DataConnection

class IPScope:

    ipScopeTable = "dbo.IPScope"
    scopeIDColumn = "ScopeID"
    ipScopeColumn = "IPScope"
    cityIDColumn = "CityID"

    def __init__(self, scopeID, ipScope, cityID):
            self.scopeID = scopeID
            self.ipScope = ipScope
            self.cityID = cityID

    def returnAddresses(self, ipScopeColumn, ipScopeTable, scopeIDColumn, returnScopeID):
        self.queryDatabase(ipScopeColumn, ipScopeTable, scopeIDColumn, returnScopeID)


    def queryDatabase(self, selectStatement, fromStatement, attributeColumnName, attributeValue):
        connection = DataConnection

        query = "SELECT " + selectStatement + "FROM " + fromStatement + "WHERE " + attributeColumnName + " = " + attributeValue

        connection.runQuery(self, query)