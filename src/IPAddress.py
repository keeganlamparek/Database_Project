from ipaddress import ip_network
from IPTable import IPTable
from DataConnection import DataConnection

class IPAddress(IPTable):

    ipAddressTable = "IPAddress"
    scopeIDColumn = "ScopeID"
    ipAddressColumn = "IPAddress"

    def askForInput(self):
        print()
        print("Choose a funtion below")
        print("1: Reveal address's assoiciated scope")
        userInput = input("Enter a number or q to go back: ")

        if(userInput == "1"):
            self.findAddressScope()
            self.askForInput()
        elif(userInput == "q"):
            return

    def findAddressScope(self):

        connection = DataConnection()

        address = input("Enter IP address: ")

        query = "SELECT " + self.scopeIDColumn + " FROM " + self.ipAddressTable + " WHERE " + self.ipAddressColumn + " = " + address

        try:
            result = connection.runQuery(query)
            print(result)

        except:
            print("Not a valid address or address does not exits")


        


    def insertAddress(self, ipScope, scopeID):

        insertInto = " INSERT INTO IPAddress(IPAddress, ScopeID) VALUES"
        query = insertInto
        allAddresses = self.parseScope(ipScope)

        overflowCounter = 0

        for address in allAddresses:
            
            query += "('" + address + "', " + scopeID + "),"
            overflowCounter += 1
            if (overflowCounter >= 1000):
                query = query[:-1]
                query += "; "
                query += insertInto
                overflowCounter = 0

        query = query[:-1]
        query += ";"

        return query

    def deleteAddresses(self, deleteQuery):

        deleteQuery += "DELETE FROM " + self.ipAddressTable + " WHERE " + self.scopeIDColumn + " = " + "?" + " ;"
        return deleteQuery

    def parseScope(self, scopeToParse):

        returnList = list()
        listOfAddresses = list(ip_network(scopeToParse).hosts()) 
        
        for ip in listOfAddresses:
            returnList += ip.exploded.split("'")
            

        return returnList
