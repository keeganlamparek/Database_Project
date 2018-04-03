from DataConnection import DataConnection
from ipaddress import ip_network

class IPScope():

    ipScopeTable = "IPScope"
    scopeIDColumn = "ScopeID"
    ipScopeColumn = "IPScope"
    cityIDColumn = "CityID"

    def __init__(self, scopeID):
        self.scopeID = scopeID
        
    @classmethod
    def insertScope(self):

        newScopeID = input("Enter the ID for the new scope: ")
        newScope = input('Enter the new IP scope: ')
        newCityID = input('Enter the City ID: ')
          
        connection = DataConnection()

        query = "INSERT INTO " + IPScope.ipScopeTable

        query += "(" + IPScope.scopeIDColumn + "," + IPScope.ipScopeColumn + "," + IPScope.cityIDColumn + ")"
        query += "VALUES(?, ?, ?)"
        values = [newScopeID, newScope, newCityID]

        connection.updateData(query, values)
        connection.closeConnection()
        
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
    
    @classmethod
    def deleteScope(self):

        print("What scope would you like to delete?")
        self.displayIPScopeTable(self)
        scopeToDelete = input("Select ScopeID to delete: ")

        query = "DELETE FROM " + self.ipScopeTable + " WHERE " + self.scopeIDColumn + " = " + "?"
        values = [scopeToDelete]
        connection = DataConnection()
        connection.updateData(query, values)
        connection.closeConnection()

        print("Deleting...")
        self.displayIPScopeTable(self)

    @classmethod
    def updateScope(self):

        print("What IP scope would you like to update?")
        self.displayIPScopeTable(self)

        scopeToUpdate = input("Select by ScopeID: ")
        updatedScope = input("Enter updated scope: ")
        query = "UPDATE " + self.ipScopeTable + " SET " + self.ipScopeColumn + " = "  + "?" + " WHERE " + self.scopeIDColumn + " = " + "?"
        
        print("Updating IP scope...")
        values = [updatedScope, scopeToUpdate]
        connection = DataConnection()
        connection.updateData(query, values)
        connection.closeConnection
       
        print("Values Updated:")
        self.displayIPScopeTable(self)
        
    def displayIPScopeTable(self):
        
        connection = DataConnection()
        query = "SELECT * FROM " + self.ipScopeTable 

        allScopes = connection.runQuery(query)

        print("ScopeID ", "    IPScope ", "    CityID")
        for row in allScopes:
            print("  ", row.ScopeID, "     ", row.IPScope, "     ", row.CityID)

        connection.closeConnection()


        
           







