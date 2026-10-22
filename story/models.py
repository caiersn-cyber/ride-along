from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone
from mdeditor.fields import MDTextField

# Create your models here.

class AddStory(models.Model):
    '''
        创建故事表
        包含user用户名，add_date初始创建时间,modify_date最新修改时间，title标题，
        story_content故事内容,location关联地点，图像image；
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=100)
    add_date = models.DateTimeField(default=timezone.now)
    modify_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, default='null')
    story_absrtact = models.TextField(default='关于贵州的故事分享')
    story_content = MDTextField(default='这是我的分享')
    location = models.CharField(max_length=200)  # Added location field
    image = models.ImageField(upload_to='static/stories/')

    def __str__(self):
        res = str(self.user) +':'+ self.title
        return res

    def save(self, *args, **kwargs):
        if not self.image:
            self.image = 'default_image.jpg'  # Assign default image if no image was submitted
        super().save(*args, **kwargs)

