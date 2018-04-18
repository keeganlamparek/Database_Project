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
          
        allAddresses = self.parseScope(self, newScope)

        connection = DataConnection()

        query = "BEGIN TRY BEGIN TRAN "
        query += "INSERT INTO " + IPScope.ipScopeTable

        query += "(" + IPScope.scopeIDColumn + "," + IPScope.ipScopeColumn + "," + IPScope.cityIDColumn + ")"
        query += "VALUES(?, ?, ?); "
        
        query += "INSERT INTO IPAddress(IPAddress, ScopeID) VALUES"

        for address in allAddresses:
            query += "('" + address + "', " + newScopeID + "),"

        query = query[:-1]
        query += ";"

        query += " COMMIT TRAN END TRY BEGIN CATCH ROLLBACK TRAN END CATCH;"
        
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
        self.displayIPScopeTable()
        scopeToDelete = input("Select ScopeID to delete: ")

        query = "DELETE FROM " + self.ipScopeTable + " WHERE " + self.scopeIDColumn + " = " + "?"
        values = [scopeToDelete]
        connection = DataConnection()
        connection.updateData(query, values)
        connection.closeConnection()

        print("Deleting...")
        self.displayIPScopeTable()

    @classmethod
    def updateScope(self):

        print("What IP scope would you like to update?")
        self.displayIPScopeTable()

        scopeToUpdate = input("Select by ScopeID: ")
        updatedScope = input("Enter updated scope: ")
        query = "UPDATE " + self.ipScopeTable + " SET " + self.ipScopeColumn + " = "  + "?" + " WHERE " + self.scopeIDColumn + " = " + "?"
        
        print("Updating IP scope...")
        values = [updatedScope, scopeToUpdate]
        connection = DataConnection()
        connection.updateData(query, values)
        connection.closeConnection
       
        print("Values Updated:")
        self.displayIPScopeTable()

    @classmethod    
    def displayIPScopeTable(self):
        
        connection = DataConnection()
        query = "SELECT * FROM " + self.ipScopeTable 

        allScopes = connection.runQuery(query)

        print("ScopeID ", "    IPScope ", "    CityID")
        for row in allScopes:
            print("  ", row.ScopeID, "     ", row.IPScope, "     ", row.CityID)

        connection.closeConnection()


        
           







