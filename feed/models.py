from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    class Meta:
        db_table ="my_post"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default="unknown", on_delete=models.CASCADE)
    post_title = models.TextField(default = "write title") #게시글 제목
    post_content = models.TextField(default = "write content") #게시글 내용
    post_image = models.TextField(default = "https://www.spectory.net/src/images/noImg.gif")
    created_at = models.DateTimeField(auto_now_add=True) # 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 수정시간
    
    # user_nickname = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
