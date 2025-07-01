# Stores app-wide settings (like the database URI)
import os 
class Config:

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://admin:dhia@localhost:5432/bizza")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
