import requests
import json
import ast
from createDBInstance import db, RichMenu



with open('Config.json', 'r') as f:
    config_dict = json.load(f)

# Authorization is Channel access token
headers = {"Authorization":"Bearer " + config_dict['CHANNEL_ACCESS_TOKEN']
           ,"Content-Type":"application/json"}

body = {
    "size": {
      "width": 2500,
      "height": 843
    },
    "selected": False,
    "name": "richMenuDemo2",
    "chatBarText": "Demo2",
    "areas": [
      {
        "bounds": {
          "x": 0,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "message",
          "label": "文字",
          "text": "來支MV"
        }
      },
      {
        "bounds": {
          "x": 833,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "uri",
          "label": "網址",
          "uri": "https://blow.streetvoice.com/"
        }
      },
      {
        "bounds": {
          "x": 1666,
          "y": 0,
          "width": 833,
          "height": 843
        },
        "action": {
          "type": "postback",
          "label": "都不要",
          "data": "richMenuDemo1"
        }
      }
   ]
}

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

richMenuDict = ast.literal_eval(req.text)
newRichMenu = RichMenu(name = body["name"],content = richMenuDict["richMenuId"])
db.session.add(newRichMenu)
db.session.commit()

print(req.text)
