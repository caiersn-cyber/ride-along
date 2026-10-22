from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from story.models import AddStory
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

from django.db.models import Q


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'账号成功创建！')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'账号成功更新！')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)


def temp(request):
    return render(request, 'users/profile_trip.html')


# class StoryListView(ListView):
#      #model = AddStory
#      template_name = 'users/profile_story.html'
#      context_object_name = 'stories'
#      def get_queryset(self):
#         stories = AddStory.objects.filter(
#             Q(user=request.user.username)
#         )
#         return stories


def personal_story_show(request):
     stories = AddStory.objects.filter(Q(user=request.user))
     return render(request, 'users/profile_story.html', {'stories': stories})