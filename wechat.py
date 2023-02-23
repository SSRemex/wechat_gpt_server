import hashlib
import time

from config import WECHAT_TOKEN
import xml.etree.ElementTree as ET


def wechat_check(wechat_data: dict):
    """
    用于微信初始化校验
    :param wechat_data: 微信发送的GET参数数据
    :return:
    """
    timestamp = wechat_data.get("timestamp")
    nonce = wechat_data.get("nonce")
    concat_sorted = sorted([WECHAT_TOKEN, timestamp, nonce])
    concat_sorted = "".join(concat_sorted)
    encode_str = hashlib.sha1(concat_sorted.encode("utf8")).hexdigest()
    if encode_str == wechat_data.get("signature"):
        return True
    else:
        return False


def xml_decode(xml):
    """

    :param xml:
    :return: {  'ToUserName': 'gh_c70929992471',
                'FromUserName': 'olsz16KhdjlYNyxgoLG_CaPeGSFs',
                'CreateTime': '1677080360',
                'MsgType': 'text',
                'Content': '你好',
                'MsgId': '24010015459797479'}
    """
    xml_str = xml.decode("utf8")
    root = ET.fromstring(xml_str)
    msg_info = {}
    for child in root:
        msg_info[child.tag] = child.text

    return msg_info


def xml_encode(target, open_id, content):

    xml = f"""<xml>\n<ToUserName><![CDATA[{target}]]></ToUserName>\n<FromUserName><![CDATA[{open_id}]]></FromUserName>\
\n<CreateTime>{int(time.time())}</CreateTime>\n<MsgType><![CDATA[text]]></MsgType>\n\
<Content><![CDATA[{content}]]></Content>\n</xml>""".encode("utf8")

    return xml
