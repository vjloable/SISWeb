from dotenv import load_dotenv
from flask_session import Session

from app import create_app
from app.services.database_service import DatabaseService
from app.services.cloud_service import CloudService

load_dotenv()

database_service = DatabaseService()
database_connection = database_service.connect()

cloud_service = CloudService()
cloud_service.configure()

app = create_app(database_connection)
Session(app)

@app.teardown_appcontext
def teardown_db(exception=None):
    database_connection.close()

if __name__ == "__main__":
    app.run()