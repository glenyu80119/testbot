import json
from linebot import (
    LineBotApi, WebhookHandler
)
from createDBInstance import db
from RichMenu import RichMenu

with open('Config.json', 'r') as f:
    config_dict = json.load(f)

# Channel access token
line_bot_api = LineBotApi(config_dict['CHANNEL_ACCESS_TOKEN'])

line_bot_api.delete_rich_menu('richmenu-77b63d87ac18c77137cab9b4af532865')