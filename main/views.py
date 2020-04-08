from django.shortcuts import render, HttpResponse
from hjs_cmfz import settings
from utils.send_mess import yunpian
from utils import send_mess
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from utils import random_number

e = random_number.random_num()

def main(request):
    return render(request, "main.html")


def login_form(request):
    return render(request, "login.html")

@csrf_exempt
def get_code(request):
    mobile = request.POST.get("mobile")
    if mobile:
        code = e
        print(e)
        yun = yunpian(settings.APIKEY)
        # status = yun.send_message(code=code, phone=mobile)
        # print(status)
        pass
    return HttpResponse("success")