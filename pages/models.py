from django.db import models
from mdeditor.fields import MDTextField
from city.models import City
# Create your models here.

class Popular_project(models.Model):
    '''
        创建故事表
        包含user用户名，add_date初始创建时间,modify_date最新修改时间，title标题，
        story_content故事内容,location关联地点，图像image；
    '''


    project_name = models.CharField(max_length=200, default='null')
    absrtact = models.TextField()
    body = MDTextField(default='')
    location = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)  # Added location field
    cover_image = models.ImageField(upload_to='pages/images/project_exp/cover')

    def __str__(self):
        res = str(self.user) +':'+ self.title
        return res

