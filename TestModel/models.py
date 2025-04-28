from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
    test = models.CharField(max_length=20)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()

    # sex = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, )
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)  # id 会自动创建,可以手动写入
    title = models.CharField(max_length=32)  # 书籍名称
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 书籍价格
    publish = models.CharField(max_length=32)  # 出版社名称
    pub_date = models.DateField()  # 出版时间

    # avatarurl = models.ImageField('头像', max_length=512, null=False, default='')

    def __unicode__(self):
        return self.price


class test3(models.Model):
    # id=models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)

    # def __unicode__(self):
    #     return self.name


class test2(models.Model):
    # id=models.CharField(max_length=10)
    t1 = models.CharField(max_length=20)
    t2 = models.ImageField('头像', max_length=512, null=False, default='')

# class User(models.Model):
#     mobile = models.CharField(max_length=11, unique=True)
#     password_hash = models.CharField(max_length=255)
#     sms_code = models.CharField(max_length=6, null=True)
#     sms_code_expire = models.DateTimeField(null=True)

    # def set_password(self, password):
    #     self.password_hash = hashlib.sha256(password.encode()).hexdigest()