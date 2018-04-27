from DataConnection import DataConnection
from IPAddress import IPAddress
from IPTable import IPTable
import socket

class IPScope(IPTable):

    ipScopeTable = "IPScopeTable"
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
        print("Scopes with a slash lower than a.b.c.d/21 don't work at this moment.")
        newScope = input('Enter the new IP scope: ')
        newCityID = input('Enter the City ID: ')


        if(cls.is_a_valid_ip_address(cls, newScope)):
            connection = DataConnection()

            query = "BEGIN TRY BEGIN TRAN "
            query += "INSERT INTO " + cls.ipScopeTable

            query += "(" + cls.scopeIDColumn + "," + cls.ipScopeColumn + "," + cls.cityIDColumn + ")"
            query += "VALUES(?, ?, ?); "

            ipAddress = IPAddress()
            query += ipAddress.insertAddress(newScope, newScopeID)

            query += " COMMIT TRAN END TRY BEGIN CATCH ROLLBACK TRAN END CATCH;"
            
            values = [newScopeID, newScope, newCityID]
        
            connection.updateData(query, values)
            connection.closeConnection()
        else:
            
            print()
            print("Please type a valid address!")
            print()
            #Program will keep asking until valid IP scope is entered
            cls.insertScope()  

    def deleteScope(self):
      
        self.displayIPScopeTable()
        scopeID = input("Select ScopeID to delete: ")

        query = "BEGIN TRY BEGIN TRAN "
        ipAddress = IPAddress()
        query += ipAddress.deleteAddresses()
        query += "DELETE FROM " + self.ipScopeTable + " WHERE " + self.scopeIDColumn + " = " + "?" + " ; "

        query += " COMMIT TRAN END TRY BEGIN CATCH ROLLBACK TRAN END CATCH;"

        values = [scopeID, scopeID]  #2nd scopeID comes from ipAddress.deleteAddresses()

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

        if(cls.is_a_valid_ip_address(cls, updatedScope)):
            query = "UPDATE " + cls.ipScopeTable + " SET " + cls.ipScopeColumn + " = "  + "?" + " WHERE " + cls.scopeIDColumn + " = " + "?" + "; "
            
            ipAddress = IPAddress()
            query += ipAddress.deleteAddresses()

            query += ipAddress.insertAddress(updatedScope, scopeToUpdate)

            print("Updating IP scope...")
            values = [updatedScope, scopeToUpdate, scopeToUpdate] # 3rd value and ? is located from the ipAddress.deleteAddress()
            connection = DataConnection()
            connection.updateData(query, values)
            connection.closeConnection
        
            print("Values Updated:")
            cls.displayIPScopeTable()

        else:
            print()
            print("Please type a valid address!")
            print()
            #Program will keep asking until valid IP scope is entered
            cls.updateScope() 

    @classmethod    
    def displayIPScopeTable(cls):

        connection = DataConnection()
        query = "SELECT " + cls.scopeIDColumn + ", " + cls.ipScopeColumn + ", " + cls.cityIDColumn + " FROM " + cls.ipScopeTable 

        allScopes = connection.runQuery(query)

        print("ScopeID ", "    IPScope ", "    CityID")
        for row in allScopes:
            print("  ", row.ScopeID, "     ", row.IPScope, "     ", row.CityID)

        connection.closeConnection()

    def is_a_valid_ip_address(self, address):

        address = address[:-3] #delete the slash notation from the scope Ex: 10.0.0.0/21 --> 10.0.0.0

        try:
            socket.inet_pton(socket.AF_INET, address)

        except socket.error:  # not a valid address
            return False

        return True