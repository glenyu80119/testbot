from flask import Flask

from linebot import ( 
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import (
	MessageEvent,
	TestMessage,
	TextSendMessage
)

app = Flask(__name__)
line_bot_api = LineBotApi('AooJdMsRyq6LV+OgOLDwVI+GSUsbG4CwGi2mV4nBq2TQgHC6OO8odH6H1Jm0BDK01dkTH4C3JZ8CH9EdqAHZpgrw4yAKP6D4b7gofQrmVrRu5c0dAYhGT3rNgbsklKbZ0S7eUwJHE/uqnZOaGXC56wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('30d9b4930e5eaa9cac656c533977e295')

@app.route('/')
def hello():
	return 'Hello, World!'