import os
from tinydb import TinyDB, Query
from serializer import serializer



def find_allQuestions() -> list:
    """Find all deviQuestions in the database."""
    # Define the database connector
    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('allQuestions')
    # Search the database for all questions that are active
    result = db_connector.all()
    return result