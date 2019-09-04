import json

from linebot import (
    LineBotApi, WebhookHandler
)

with open('Config.json', 'r') as f:
    config_dict = json.load(f)

# Channel access token
line_bot_api = LineBotApi(config_dict['CHANNEL_ACCESS_TOKEN'])

line_bot_api.set_default_rich_menu('richmenu-75a68506f6846cbf75555098958fe78d')