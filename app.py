from flask import Flask, request
import json
import requests

global LINE_API_KEY
LINE_API_KEY = 'Bearer sl640wlzs4BMjI0OIl+orPXVN3lDfwXc9yvo9tvjiEow4ODs3+hVtQEEHclfonw/FTo+kmGc+SNKyjU0jDnTr3FLu2WzC6PUI/PiOHs9RhGfLIFt9/60UVVpxmJq37VuUdlV4ew4CXW5aboLzFTMDwdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)
 
@app.route('/')
def index():
    return 'This is chatbot server.'

@app.route('/bot', methods=['POST'])
def bot():
    replyStack = list()
   
    msg_in_json = request.get_json()
    msg_in_string = json.dumps(msg_in_json)
    
    replyToken = msg_in_json["events"][0]['replyToken']

    replyStack.append(msg_in_string)
    # reply(replyToken, msg_in_json["events"][0]["message"]["text"])
    rule = rule_base(msg_in_json["events"][0]["message"]["text"])
    reply(replyToken, rule)
    return 'OK',200

def rule_base(message_text):
    if("ราคา" in message_text):
        price = "ในส่วนของราคาถ้าเป็นกางเกงสแล็ค 300 บาทค่ะ"
        return price
    else:
        return "ไม่เข้าใจเกี่ยวกับคำถาม เราจะปรับปรุงเกี่ยวกับการตอบคำถามให้ดีขึ้นในภายหลังนะค่ะ กราบขออภัย(ok)"
    return
    
        
def reply(replyToken, textList):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    msgs.append({
            "type":"text",
            "text":textList
        })

    data = json.dumps({
        "replyToken":replyToken,
        "messages":msgs
    })
    
    requests.post(LINE_API, headers=headers, data=data)
    return

if __name__ == '__main__':
    app.run()