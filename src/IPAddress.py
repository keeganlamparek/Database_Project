from ipaddress import ip_network
from IPTable import IPTable
from DataConnection import DataConnection


class IPAddress(IPTable):

    ipAddressTable = "IPAddressTable"
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

        try:
            selectFromIPAddressTableQuery = "SELECT " + self.scopeIDColumn + " FROM " + self.ipAddressTable + " WHERE " + self.ipAddressColumn + " = '" + address + "'"
            result = connection.runQuery(selectFromIPAddressTableQuery)
            row = result.fetchone()
            scopeID = row.ScopeID
            
            query = "SELECT " + " IPScope " + " FROM " + "IPScopeTable" + " WHERE " + self.scopeIDColumn + " = " + str(scopeID)
            result = connection.runQuery(query)
            row = result.fetchone()
            associatedScope = row.IPScope

            print("The associated scope is: " + associatedScope)

            connection.closeConnection()

        except:
            print("Not a valid address or address does not exits")

    def insertAddress(self, ipScope, scopeID):

        insertInto = " INSERT INTO "+ self.ipAddressTable + " (IPAddress, ScopeID) VALUES"
        query = insertInto
        allAddresses = self.parseScope(ipScope)

        sqlInsertLimitation = 1000
        overflowCounter = 0

        for address in allAddresses:
            
            query += "('" + address + "', " + scopeID + "),"
            overflowCounter += 1
            if (overflowCounter >= sqlInsertLimitation):
                query = query[:-1]
                query += "; "
                query += insertInto
                overflowCounter = 0

        query = query[:-1]
        query += ";"

        return query

    def deleteAddresses(self):

        deleteQuery = " DELETE FROM " + self.ipAddressTable + " WHERE " + self.scopeIDColumn + " = " + "?" + " ;"
        return deleteQuery

    def parseScope(self, scopeToParse):

        returnList = list()
        listOfAddresses = list(ip_network(scopeToParse).hosts()) # returns a list of IP addresses
        
        for ip in listOfAddresses:
            returnList += ip.exploded.split("'")
            
        return returnList
