# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
import random
from datetime import datetime, timedelta

class SmsCodeView(APIView):
    def post(self, request):
        mobile = request.data['mobile']
        code = ''.join(random.choices('0123456789', k=6))
        # 实际应调用短信服务商API
        User.objects.update_or_create(
            mobile=mobile,
            defaults={'sms_code': code, 'sms_code_expire': datetime.now()+timedelta(minutes=5)}
        )
        return Response({'code': 0})

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        user = User.objects.get(mobile=data['mobile'])
        if user.sms_code != data['sms_code'] or user.sms_code_expire < datetime.now():
            return Response({'code': 400, 'msg': '验证码错误'})
        user.set_password(data['password'])
        user.save()
        return Response({'code': 0})