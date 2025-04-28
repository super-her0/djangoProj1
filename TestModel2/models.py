# models.py
from django.db import models
import hashlib

class User(models.Model):
    mobile = models.CharField(max_length=11, unique=True)
    password_hash = models.CharField(max_length=255)
    sms_code = models.CharField(max_length=6, null=True)
    sms_code_expire = models.DateTimeField(null=True)

    def set_password(self, password):
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()