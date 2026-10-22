from django.shortcuts import render, redirect
from .forms import StoryForm
from .models import AddStory
import markdown
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# 创建故事页面
@login_required
def story_add(request):
    if request.method == 'POST':
        # form = StoryForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        #     return redirect('story_list')
        story = AddStory()
        story.user = request.user
        story.title = request.POST.get('title')
        story.story_absrtact = request.POST.get('story_absrtact')
        story.story_content = request.POST.get('story_content')
        if request.POST.get('location'):
            story.location = request.POST.get('location')
        # if request.FILES.get('image'):
        #     story.image = request.FILES['image']
        # else:
        #     default_image_path = 'story/static/image.jpg'
        #     fs = FileSystemStorage(location=settings.MEDIA_ROOT)
        #     with open(default_image_path, 'rb') as f:
        #         default_image = File(f)
        #         story.image = fs.save('stories/default_image.jpg', default_image)
        story.image = request.FILES.get('image')
        story.save()
        return redirect('story_list')
    else:
        return render(request, 'story/add_story.html')


# 展示故事信息页面
def story_list(request):
    stories = AddStory.objects.all()
    return render(request, 'story/story_list.html', {'stories': stories})

# 测试页面
def story_show(request):
    return render(request, 'story/story_show.html')

# 删除界面
def story_delete(request, pk):
    story = AddStory.objects.get(pk=pk)
    story.delete()
    return redirect('story_list')

# 故事更新编辑界面
def story_update(request, pk):

    if request.method == 'POST':
        story = AddStory.objects.get(pk=pk)
        # story = AddStory()
        story.user = request.user
        story.title = request.POST.get('title')
        story.story_absrtact = request.POST.get('story_absrtact')
        story.story_content = request.POST.get('story_content')
        if request.POST.get('location'):
            story.location = request.POST.get('location')
        story.image = request.FILES.get('image')
        story.save()
        return redirect('story_list')
    else:
        return render(request, 'story/story_update.html')

# 单个故事详情页
def story_each_content(request, pk):
    story = AddStory.objects.get(pk=pk)
    story.story_content = markdown.markdown(story.story_content,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    if story.user != request.user:  # 验证访问页面的用户是否是拥有页面的用户
        return render(request, 'story/story_each_content_without_user.html', {'story': story})
    else:
        return render(request, 'story/story_each_content.html', {'story': story})