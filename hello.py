from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from os import environ

from linebot import ( 
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import (
	MessageEvent, TextMessage, TextSendMessage, PostbackEvent
)

from richMenu.createDBInstance import RichMenu
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///richMenu/richMenu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


CHANNEL_ACCESS_TOKEN = environ.get('CHANNEL_ACCESS_TOKEN')
CHANNEL_SECRET = environ.get('CHANNEL_SECRET')

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="I know nothing but a good song now, https://reurl.cc/4Edb2"))

@handler.add(PostbackEvent)
def handle_message(event):
    rm = RichMenu.query.filter_by(name = event.postback.data).first()
    if rm:
        line_bot_api.link_rich_menu_to_user(event.source.user_id, rm.content)


if __name__ == "__main__":
    app.run()