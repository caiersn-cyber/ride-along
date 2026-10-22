from django import forms
from .models import AddStory
from mdeditor.fields import MDTextFormField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import get_user

# user = get_user(request)
#
# # Finally, we can get the username of the current user using the username attribute of the User object.
# username = user.username

class StoryForm(forms.ModelForm):

    class Meta:
        model = AddStory
        fields = ['user', 'title', 'story_absrtact', 'story_content', 'location', 'image']

        labels = {
            'user': '用户名',
            'title': '故事标题',
            'story_absrtact': '故事摘要',
            'story_content': '故事正文',
            'location': '故事关联地点',
            'image': '相关图片',
        }

    # def clean_user(self):
    #     user_input = self.cleaned_data['user']
    # #     #print(self.clean_user['user'])
    # #     #exp_username = User.objects.filter(pk=int(user_input))
    # #     print(user_input)
    # #     print(User)
    # #     #print(model_to_dict(User.username))
    #     if user_input != username:
    #         raise ValidationError('用户名输入错误！')
    #     return user_input
