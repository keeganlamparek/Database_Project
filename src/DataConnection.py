from SimpleDataSource import SimpleDataSource

class DataConnection:
    def __init__(self):
        self.connection = SimpleDataSource.getConnection()

    def runQuery(self, query):
        cursor = self.connection.cursor()
        resultSet = cursor.execute(query)
        return resultSet

    def updateData(self, query, arguments = []):
        cursor = self.connection.cursor()
        cursor.execute(query, arguments)
        self.connection.commit()
        
    def closeConnection(self):
        self.connection.close()
