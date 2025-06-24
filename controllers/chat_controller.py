# controllers/chat_controller.py
import requests
from flask import jsonify, render_template, request
from models.chat_model import Chat, db
from forms.chat_form import ChatForm
from config import Config

def is_origin_question(message):
    message = message.lower()
    trigger_keywords = [
        "ai tạo", "ai phát triển", "do ai", "thuộc về ai", "sản phẩm của ai",
        "bạn là ai", "bạn là gì", "trợ lý của ai", "bạn thuộc về",
        "gemini", "google", "mô hình ngôn ngữ", "nền tảng",
        "bạn hoạt động như thế nào", "bạn học từ đâu", "dữ liệu nào",
        "huấn luyện bạn", "bạn có nhớ", "bạn có thể nhớ", "bạn nhớ không",
        "trí nhớ", "bạn có truy cập internet", "bạn có tìm kiếm",
        "tìm kiếm thông tin", "cập nhật thông tin", "học được từ đâu"
    ]
    return any(kw in message for kw in trigger_keywords)

def get_gemini_response(message):
    if is_origin_question(message):
        return "Tôi là chatbot do Mr. Nhan (mycode.edu.vn) tạo ra."
    
    try:
        response = requests.post(Config.GEMINI_API_URL, json={
            "contents": [{"role": "user", "parts": [{"text": message}]}]
        }, headers={"Content-Type": "application/json; charset=utf-8"})
        response.raise_for_status()
        gemini_reply = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        
        forbidden_keywords = ["google", "gemini", "mô hình ngôn ngữ", "language model", "ai của google"]
        if any(word in gemini_reply.lower() for word in forbidden_keywords):
            return "Tôi là chatbot do Mr. Nhan (mycode.edu.vn) tạo ra."
        
        return gemini_reply
    except Exception as e:
        return f"Error: {e}"

# def index():
#     chats = Chat.query.order_by(Chat.timestamp.asc()).all()
#     form = ChatForm()
#     return render_template('chat.html', chats=chats, form=form)

# def send_message():
#     message = request.form.get('message')
#     if not message:
#         return jsonify({"error": "No message"}), 400
#     response = get_gemini_response(message)
#     chat = Chat(user_message=message, api_response=response)
#     db.session.add(chat)
#     db.session.commit()
#     return jsonify({"user_message": message, "api_response": response}), 200


# def new_chat():
#     return render_template('chat.html')



def index():
    form = ChatForm() 
    question = request.args.get('new_question', 'default')
    chats = Chat.query.filter_by(chat_question=question).order_by(Chat.timestamp.asc()).all()
    sessions = db.session.query(Chat.chat_question).distinct().all()
    return render_template('chat.html', chats=chats, form=form,current_session=question, sessions=[s[0] for s in sessions])


def send_message():
    message = request.form.get('message')
    new_question = request.form.get('new_question', 'default')
    if not message:
        return jsonify({"error": "No message"}), 400
    response = get_gemini_response(message)
    chat = Chat(user_message=message, api_response=response,chat_question=new_question)
    db.session.add(chat)
    db.session.commit()
    return jsonify({"user_message": message, "api_response": response}), 200

from datetime import datetime
def new_chat():
    new_question = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    return jsonify({"new_question": new_question}), 200


from flask import url_for
def delete_chat():
    new_question = request.form.get('new_question')
    if new_question:
        Chat.query.filter_by(chat_question=new_question).delete()
        db.session.commit()
        return jsonify({"status": "Deleted", "redirect": url_for('chat.index')}), 200
    return jsonify({"error": "No session"}), 400


def edit_message(chat_id):
    message = request.form.get('message')
    if not message:
        return jsonify({"error": "No message"}), 400
    chat = Chat.query.get_or_404(chat_id)
    chat.user_message, chat.api_response, chat.timestamp = message, get_gemini_response(message), datetime.utcnow()
    db.session.commit()
    return jsonify({"user_message": message, "api_response": chat.api_response, "chat_id": chat.id})


def home():
    return render_template('home.html')