from config import Config
from routes.routes import  chat_router
from flask import Flask
from models.chat_model import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Đăng ký route
app.register_blueprint( chat_router)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
        
