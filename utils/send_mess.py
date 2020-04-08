import requests


class yunpian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        # 使用云片网提供的替三方接口完成短信发送
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_message(self, phone, code):
        parmas = {
            'apikey': self.api_key,
            'mobile': phone,
            'text': "【胡俊生test】您的验证码是{code}".format(code=code)
        }
        req = requests.post(self.single_send_url, data=parmas)
        print(req)


if __name__ == '__main__':
    y = yunpian("22cde034573b83d38c8541908c501bdc")
    y.send_message("17641525210", "123456")