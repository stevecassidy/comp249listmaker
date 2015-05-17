import sqlite3


class COMP249Db():
    '''
    Provide an interface to the database for a COMP249 web application
    '''

    def __init__(self, dbname="comp249.db"):
        '''
        Constructor, database name is an optional parameter
        the default 'comp249.db' is suitable for most cases.
        '''
        
        self.dbname = dbname
        self.conn = sqlite3.connect(self.dbname)
        ### ensure that results returned from queries are strings rather
        ### than unicode 
        self.conn.text_factory = str
        
    def cursor(self):
        """Return a cursor on the database"""
        
        return self.conn.cursor()
    
    def commit(self):
        """Commit pending changes"""
        
        self.conn.commit()
        

if __name__ == "__main__":
    
    db = COMP249Db()
    