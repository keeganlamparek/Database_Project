from ipaddress import ip_network
from IPTable import IPTable

class IPAddress(IPTable):

    
    def insertAddress(self, query):


        insertInto = "INSERT INTO IPAddress(IPAddress, ScopeID) VALUES"
        query += insertInto
        allAddresses = self.parseScope(self.ipScope)

        overflowCounter = 0

        for address in allAddresses:
            
            query += "('" + address + "', " + self.scopeID + "),"
            overflowCounter += 1
            print(overflowCounter)
            if (overflowCounter >= 1000):
                query = query[:-1]
                query += "; "
                query += insertInto
                overflowCounter = 0


        query = query[:-1]
        query += ";"

        return query

    def parseScope(self, scopeToParse):

        returnList = list()
        listOfAddresses = list(ip_network(scopeToParse).hosts()) 
        
        for ip in listOfAddresses:
            returnList += ip.exploded.split("'")
            
        return returnList
