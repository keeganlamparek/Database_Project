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
    
        #query += "INSERT INTO IPAddress(IPAddress, ScopeID) VALUES"

        ipAddresses = IPAddress(newScopeID, newScope)
        query = ipAddresses.insertAddress(query)


      #  for address in allAddresses:
      #      query += "('" + address + "', " + newScopeID + "),"

      #  query = query[:-1]
      #  query += ";"

        query += " COMMIT TRAN END TRY BEGIN CATCH ROLLBACK TRAN END CATCH;"
        
        values = [newScopeID, newScope, newCityID]

        connection.updateData(query, values)
        connection.closeConnection()
        
    @classmethod
    def returnAddresses(cls, scopeID):
        scopeAddress = cls.selectQuery(cls, cls.ipScopeColumn, cls.scopeIDColumn, scopeID)
        addresses = cls.parseScope(cls, scopeAddress)
        return addresses

    def selectQuery(self, selectStatement, whereColumn, attributeValue):
        connection = DataConnection()

        query = "SELECT " + selectStatement + " FROM " + self.ipScopeTable + " WHERE " + whereColumn + " = " + attributeValue

        result = connection.runQuery(query)
        return result.fetchone()[0]

    @classmethod
    def deleteScope(cls):

        print("What scope would you like to delete?")
        cls.displayIPScopeTable()
        scopeToDelete = input("Select ScopeID to delete: ")

        query = "DELETE FROM " + cls.ipScopeTable + " WHERE " + cls.scopeIDColumn + " = " + "?"
        values = [scopeToDelete]
        connection = DataConnection()
        connection.updateData(query, values)
        connection.closeConnection()

        print("Deleting...")
        cls.displayIPScopeTable()

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


        
           







