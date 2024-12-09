class Config:
    # SQLite URI for a local database file
    SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'  # Relative path to the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking
    SECRET_KEY = 'your_secret_key'  # Replace with a secure secret key
