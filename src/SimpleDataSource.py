import pyodbc

class SimpleDataSource: 

    @classmethod
    def getConnection(cls):

        return pyodbc.connect(DRIVER = '{SQL Server}', SERVER = 'localhost', DATABASE = 'ISP_Database')
