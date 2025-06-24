# forms/chat_form.py
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ChatForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired()])
