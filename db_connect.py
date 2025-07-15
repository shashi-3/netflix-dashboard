"""
class DatabaseConnection:
    def __init__(self, db_name='netflix_data.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()
        self.cursor.close()

    def c(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()


# data reading 1 function
# delete on db 
"""
from sqlalchemy import create_engine,text
import os
from dotenv import load_dotenv
load_dotenv()

# Replace with your actual SQL Server details
server = os.getenv('DB_SERVER')
database = os.getenv('DATABASE')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
driver = 'ODBC Driver 17 for SQL Server'

connection_string = (
    f"mssql+pyodbc://{username}:{password}@{server}/{database}"
    f"?driver={driver.replace(' ', '+')}"
)
print("Connection String:", connection_string)

engine = create_engine(connection_string)
# You cannot use sqlite3 to connect to a SQL Server database.
# Use SQLAlchemy's engine (already created above) for database operations.
# Example: To test the connection, you can try:
with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print(result.fetchone())


