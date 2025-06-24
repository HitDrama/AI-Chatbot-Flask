from flask import Blueprint


#chat
from controllers.chat_controller import index, send_message,new_chat,delete_chat,edit_message,home
# Create Blueprint
chat_router = Blueprint("chat", __name__)
# Register routes by mapping to controller functions
chat_router.route("/")(home)
chat_router.route("/chat-bot")(index)
chat_router.route("/send_message", methods=["POST"])(send_message)
chat_router.route("/new_chat", methods=["POST"])(new_chat)
chat_router.route("/delete_chat", methods=["POST"])(delete_chat)
chat_router.route("/edit_message/<int:chat_id>", methods=["POST"])(edit_message)