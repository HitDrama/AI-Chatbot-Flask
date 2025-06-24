class Config:
    SECRET_KEY = 'uytrdcvg654z23456ygf'
    GOOGLE_API_KEY = KEY_YOU_GET_FROM_GOOGLE
    GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key={GOOGLE_API_KEY}"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost/chatgemini"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
