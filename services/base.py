from sqlalchemy.orm import sessionmaker
from config.engine import engine

class DbConnection:    
    def __init__(self):
        self.session = None #Dbconnection class initialises without a session

    @property #property decorator ensures self.session is only created when accessed for the first time
    def connection(self):
        if self.session is None:    
            Session = sessionmaker(bind=engine) #create new SQLAlchemy session bound to the engine
            self.session = Session()
        return self.session #returns an active session