from flask import Flask, request, abort

from linebot import ( 
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import (
	MessageEvent, TextMessage, TextSendMessage,
)
app = Flask(__name__)

line_bot_api = LineBotApi('AooJdMsRyq6LV+OgOLDwVI+GSUsbG4CwGi2mV4nBq2TQgHC6OO8odH6H1Jm0BDK01dkTH4C3JZ8CH9EdqAHZpgrw4yAKP6D4b7gofQrmVrRu5c0dAYhGT3rNgbsklKbZ0S7eUwJHE/uqnZOaGXC56wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('30d9b4930e5eaa9cac656c533977e295')

@app.route('/')
def hello():
	return 'Hello, World!'

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
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()