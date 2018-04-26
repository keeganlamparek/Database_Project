from DataConnection import DataConnection
from IPAddress import IPAddress
from IPTable import IPTable

class IPScope(IPTable):

    ipScopeTable = "IPScope"
    scopeIDColumn = "ScopeID"
    ipScopeColumn = "IPScope"
    cityIDColumn = "CityID"
      
    def askForInput(self):
        print()
        print("Choose a funtion below")
        print("1: Show all IP scopes")
        print("2: Insert a new scope")
        print("3: Update a scope")
        print("4: Delete a scope")
        userInput = input("Enter a number or q to go back: ")

        if(userInput == "1"):
            self.displayIPScopeTable()
            self.askForInput()

        elif(userInput == "2"):
            self.insertScope()
            self.askForInput()
        
        elif(userInput == "3"):
            self.updateScope()
            self.askForInput()

        elif(userInput == "4"):
            self.deleteScope()
            self.askForInput()

        elif(userInput == "q"):
            return
        
        else:
            print()
            print("Please enter a valid funtion.")
            print()
            self.askForInput()

    @classmethod
    def insertScope(cls):

        newScopeID = input("Enter the ID for the new scope: ")
        print("Scopes lower than a /21 don't work at this moment.")
        newScope = input('Enter the new IP scope: ')
        newCityID = input('Enter the City ID: ')
          
        connection = DataConnection()

        query = "BEGIN TRY BEGIN TRAN "
        query += "INSERT INTO " + IPScope.ipScopeTable

        query += "(" + IPScope.scopeIDColumn + "," + IPScope.ipScopeColumn + "," + IPScope.cityIDColumn + ")"
        query += "VALUES(?, ?, ?); "

        ipAddresses = IPAddress()
        query += ipAddresses.insertAddress(newScope, newScopeID)

        query += " COMMIT TRAN END TRY BEGIN CATCH ROLLBACK TRAN END CATCH;"
        
        values = [newScopeID, newScope, newCityID]
     
        connection.updateData(query, values)
        connection.closeConnection()

    def deleteScope(self):
      
        self.displayIPScopeTable()
        scopeID = input("Select ScopeID to delete: ")

        query = "BEGIN TRY BEGIN TRAN "
        ipAddress = IPAddress()
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


        
           







