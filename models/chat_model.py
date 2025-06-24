# models/chat_model.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_message = db.Column(db.String(500), nullable=False)
    api_response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    chat_question = db.Column(db.String(50), nullable=False)

    def __init__(self, user_message, api_response, chat_question):
        self.user_message = user_message
        self.api_response = api_response
        self.chat_question = chat_question