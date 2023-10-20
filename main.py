from flask import g
from app import create_app
from app.services.database_service import DatabaseService
from dotenv import load_dotenv

load_dotenv()
app = create_app()
database_service = DatabaseService()
database_connection = database_service.connect()

@app.before_request
def before_request():
    g.db_con = DatabaseService().connect()

@app.teardown_appcontext
def close_db_connection(exception):
    connection = getattr(g, 'db_con', None)
    if connection is not None:
        connection.close()

if __name__ == "__main__":
    app.run()