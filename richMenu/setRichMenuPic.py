import json

from linebot import (
    LineBotApi, WebhookHandler
)

with open('Config.json', 'r') as f:
    config_dict = json.load(f)


# Channel access token
line_bot_api = LineBotApi(config_dict['CHANNEL_ACCESS_TOKEN'])


# rich menu id
with open("./menuPicture/Demo1.png", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-cceecaee03e6723812632d56825d3bef", "image/png", f)