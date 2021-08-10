from django.db import models
from user.models import CustomUser

#카테고리 선택
class Category(models.Model):
    def __str__(self):
        return self.ca_name
    ca_name = models.CharField(max_length=200)

#커뮤니티 글 작성
class Community(models.Model):
    def __str__(self):
        return self.post_title

    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    post_date = models.DateTimeField()

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='community', null=True)  #커스텀 유저 모델에서 FK로 가져왔어요
    com_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='community', null=True) #위 Category에서 FK로

class CmComment(models.Model):
    def __str__(self):
        return self.cm_comment
    
    cm_id = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='cmcomment')
    cm_comment = models.CharField(max_length=100)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cmcomment', null=True)
    