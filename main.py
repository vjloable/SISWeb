from app import create_app
from app.services.database_service import DatabaseService
from dotenv import load_dotenv

load_dotenv()
app = create_app()
database_service = DatabaseService()
database_connection = database_service.connect()

@app.teardown_appcontext
def teardown_db(exception=None):
    database_connection.close()
    database_service.close()

if __name__ == "__main__":
    app.run()