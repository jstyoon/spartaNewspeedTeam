from django.db import models
# 장고 AbstractUser 모델에 필요한 필수 필드는 username, password
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
# 관리자 호환 권한의 장고 AbstractUser 모델 상속
class User(AbstractUser):  
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings') # 추가 기능입니다 M:N 팔로워 기능
