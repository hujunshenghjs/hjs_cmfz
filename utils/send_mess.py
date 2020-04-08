import requests
from hjs_cmfz import settings
from utils import random_number

d = random_number.random_num()
print(d)


class yunpian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        # 使用云片网提供的替三方接口完成短信发送
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_message(self, phone, code):
        parmas = {
            'apikey': self.api_key,
            'mobile': phone,
            'text': "【毛信宇test】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }
        req = requests.post(self.single_send_url, data=parmas)
        print(req)


if __name__ == '__main__':
    y = yunpian(settings.APIKEY)
    # y = yunpian("22cde034573b83d38c8541908c501bdc")
    # y = yunpian("041b4d9baa96c652275b632afe1619aa")
    # y = yunpian("40d6180426417bfc57d0744a362dc108")
    y.send_message("17641525210", '{}').format(d)
