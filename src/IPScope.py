from DataConnection import DataConnection
from ipaddress import ip_network

class IPScope:

    ipScopeTable = "IPScope"
    scopeIDColumn = "ScopeID"
    ipScopeColumn = "IPScope"
    cityIDColumn = "CityID"

    def __init__(self, scopeID):
        self.scopeID = scopeID
        

    @classmethod
    def returnAddresses(self, scopeID):
        scopeAddress = self.selectQuery(self, self.ipScopeColumn, self.scopeIDColumn, scopeID)
        addresses = self.parseScope(self, scopeAddress)
        return addresses

    def selectQuery(self, selectStatement, whereColumn, attributeValue):
        connection = DataConnection()

        query = "SELECT " + selectStatement + " FROM " + self.ipScopeTable + " WHERE " + whereColumn + " = " + attributeValue

        result = connection.runQuery(query)
        return result.fetchone()[0]

    def parseScope(self, scopeToParse):

        returnList = list()

        listOfAddresses = list(ip_network(scopeToParse).hosts()) 
        
        for ip in listOfAddresses:
            returnList += ip.exploded.split("'")
            
        return returnList

