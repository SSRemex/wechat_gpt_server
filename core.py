import config
from wechat import xml_decode, xml_encode

import openai
from config import OPENAI_KEY


def gpt3_api(question):
    openai.api_key = OPENAI_KEY
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=config.MAX_TOKEN,
        n=1,
        stop=None,
        temperature=config.TEMPERATURE,
        frequency_penalty=0,
        presence_penalty=0
    )

    # 从模型生成的回复中提取文本
    ai_response = response.choices[0].text.strip()

    return ai_response


def chat(xml):
    msg_info = xml_decode(xml)
    if msg_info.get("MsgType") != "text":
        content = "不支持该类型"
    else:
        content = gpt3_api(msg_info.get("Content"))

    content = content.split("\n")[0]
    response = xml_encode(target=msg_info.get("FromUserName"), open_id=msg_info.get("ToUserName"), content=content)
    return response


