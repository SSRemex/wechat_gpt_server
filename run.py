from flask import Flask, request
from wechat import wechat_check
from core import chat

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    data = request.args
    if request.method == "GET":
        if data.get("signature") is not None:
            if wechat_check(data):
                return data.get("echostr")

    if request.method == "POST":
        xml = request.data
        response = chat(xml)
        return response

    return "None"


if __name__ == '__main__':
    app.run("0.0.0.0", port=8888)

