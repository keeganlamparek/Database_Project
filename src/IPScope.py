from DataConnection import DataConnection
from IPAddress import IPAddress
from IPTable import IPTable

class IPScope(IPTable):

    ipScopeTable = "IPScope"
    scopeIDColumn = "ScopeID"
    ipScopeColumn = "IPScope"
    cityIDColumn = "CityID"
      
    @classmethod
    def insertScope(cls):

        newScopeID = input("Enter the ID for the new scope: ")
        newScope = input('Enter the new IP scope: ')
        newCityID = input('Enter the City ID: ')
          
        connection = DataConnection()

        query = "BEGIN TRY BEGIN TRAN "
        query += "INSERT INTO " + IPScope.ipScopeTable

        query += "(" + IPScope.scopeIDColumn + "," + IPScope.ipScopeColumn + "," + IPScope.cityIDColumn + ")"
        query += "VALUES(?, ?, ?); "

        ipAddresses = IPAddress(newScopeID)
        query = ipAddresses.insertAddress(query, newScope)

        query += " COMMIT TRAN END TRY BEGIN CATCH ROLLBACK TRAN END CATCH;"
        
        values = [newScopeID, newScope, newCityID]
        print(query)
        connection.updateData(query, values)
        connection.closeConnection()
        


    def selectQuery(self, selectStatement, whereColumn, attributeValue):
        connection = DataConnection()

        query = "SELECT " + selectStatement + " FROM " + self.ipScopeTable + " WHERE " + whereColumn + " = " + attributeValue

        result = connection.runQuery(query)
        return result.fetchone()[0]

    def deleteScope(self, scopeID):
      
        query = "BEGIN TRY BEGIN TRAN "
        ipAddress = IPAddress(scopeID)
        query = ipAddress.deleteAddresses(query)
        query += "DELETE FROM " + self.ipScopeTable + " WHERE " + self.scopeIDColumn + " = " + "?" + " ; "

        query += " COMMIT TRAN END TRY BEGIN CATCH ROLLBACK TRAN END CATCH;"

        values = [scopeID, scopeID]

        connection = DataConnection()
        connection.updateData(query, values)
        connection.closeConnection()

        print("Deleting...")

    @classmethod
    def updateScope(cls):

        print("What IP scope would you like to update?")
        cls.displayIPScopeTable()

        scopeToUpdate = input("Select by ScopeID: ")
        updatedScope = input("Enter updated scope: ")
        query = "UPDATE " + cls.ipScopeTable + " SET " + cls.ipScopeColumn + " = "  + "?" + " WHERE " + cls.scopeIDColumn + " = " + "?"
        
        print("Updating IP scope...")
        values = [updatedScope, scopeToUpdate]
        connection = DataConnection()
        connection.updateData(query, values)
        connection.closeConnection
       
        print("Values Updated:")
        cls.displayIPScopeTable()

    @classmethod    
    def displayIPScopeTable(cls):
        
        connection = DataConnection()
        query = "SELECT * FROM " + cls.ipScopeTable 

        allScopes = connection.runQuery(query)

        print("ScopeID ", "    IPScope ", "    CityID")
        for row in allScopes:
            print("  ", row.ScopeID, "     ", row.IPScope, "     ", row.CityID)

        connection.closeConnection()


        
           







