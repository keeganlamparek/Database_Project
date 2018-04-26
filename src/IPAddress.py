from ipaddress import ip_network
from IPTable import IPTable

class IPAddress(IPTable):

    ipAddressTable = "IPAddress"
    scopeIDColumn = "ScopeID"


    def askForInput():
        print("testing")

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
            print(ip)
            
        
        return returnList
