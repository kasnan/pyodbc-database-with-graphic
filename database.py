import pyodbc

class Db_:
    
    def __init__(self,filename):
        #path for laptop
        #path='C:/Users/kasna/Documents/vsworkspace/Pyworkspace/pyodbc-database-with-graphic/'
        #path for desktop
        path='C:/Users/kasna/Documents/workspace/vscodeFiles/Pyworkspace/pyodbc-database-with-graphic/'
        Db_.conn=pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+path+filename+';')
        Db_.cursor = Db_.conn.cursor()
    
    def testquery(self):
        Db_.cursor.execute('select * from 고객')
        for row in Db_.cursor.fetchall():
            print(row)
    
    def ExecQuery(self, query):
        Db_.cursor.execute(query)

    def FetchQuery(self, query):
        Db_.cursor.execute(query)
        return Db_.cursor.fetchall()

    def QueryResult(self, query):
        Db_.cursor.execute(query)
        
    def GetColumns(self):
        Db_.columns = [column[0] for column 
            in Db_.cursor.description]
        return Db_.columns
    
    def save(self):
        self.conn.commit()


