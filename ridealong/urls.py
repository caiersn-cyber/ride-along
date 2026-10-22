"""ridealong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from story import views as story_views
from route import views as route_views
from pages import views as page_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    # story相关URL
    path('story/add/', story_views.story_add, name='story_add'),
    path('story/list/', story_views.story_list, name='story_list'),
    path('story/show/', story_views.story_show, name='story_show'),
    path('story/delete/<int:pk>/', story_views.story_delete, name='story_delete'),
    path('story/update/<int:pk>/', story_views.story_update, name='story_update'),
    path('story/list/<int:pk>/', story_views.story_each_content, name='story_each_content'),

    # auth相关URL
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/mystory', user_views.personal_story_show, name='my_story'),
    path('profile/mytrip', user_views.temp, name='my_trip'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # route相关URL
    path('route/showroute/<str:lat1>,<str:long1>,<str:lat2>,<str:long2>', route_views.showroute, name='showroute'),
    path('route/showmap', route_views.showmap, name='showmap'),

    # page相关URL
    path('', page_views.home, name='home'),
    path('route/', page_views.route, name='route'),
    path('route/departureitems', page_views.departure_items, name='departure_items'),
    path('route/destinationitems', page_views.destination_items, name='destination_items'),
    path('city/', page_views.city, name='city'),
    path('culture/', page_views.culture, name='culture'),
    path('about/', page_views.about, name='about'),

    path('culture/project/01', page_views.culture_project_01, name='culture_project_01'),
    path('culture/project/02', page_views.culture_project_02, name='culture_project_02'),
    path('culture/project/03', page_views.culture_project_03, name='culture_project_03'),
    path('culture/project/04', page_views.culture_project_04, name='culture_project_04'),
    path('culture/project/05', page_views.culture_project_05, name='culture_project_05'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


