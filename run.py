from app import create_app
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host=os.getenv('HOST'), port=int(os.getenv('PORT')))