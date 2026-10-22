from django.shortcuts import render
from story.models import AddStory
from city.models import City, County
from route.views import showroute


def home(request):
    return render(request, 'pages/index.html')


def route(request):
    if request.method == 'POST':
        dict = request.POST
        dep_county_option = dict['departure-county']
        des_county_option = dict['destination-county']
        if dep_county_option != '-- 市辖区、县级市、县 --' and des_county_option != '-- 市辖区、县级市、县 --':
            dep_county_id = int(dict['departure-county'])
            des_county_id = int(dict['destination-county'])
            dep_county = County.objects.filter(id=dep_county_id).first()
            des_county = County.objects.filter(id=des_county_id).first()
            dep_latitude = dep_county.latitude
            dep_longitude = dep_county.longitude
            des_latitude = des_county.latitude
            des_longitude = des_county.longitude
            return showroute(request, dep_latitude, dep_longitude,
                             des_latitude, des_longitude)
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'pages/route.html', context)


def departure_items(request):
    city = request.GET.get('departure-city')
    counties = County.objects.filter(city=city)
    context = {'counties': counties}
    return render(request, 'pages/departure-items.html', context)


def destination_items(request):
    city = request.GET.get('destination-city')
    counties = County.objects.filter(city=city)
    context = {'counties': counties}
    return render(request, 'pages/destination-items.html', context)


def city(request):
    return render(request, 'pages/city.html')


def culture(request):
    stories = AddStory.objects.all()
    length = stories.count()
    result = stories[length - 4:length]
    return render(request, 'pages/culture.html', {'stories': result})


def about(request):
    return render(request, 'pages/about.html')


def culture_project_01(request):
    return render(request, 'pages/culture_project_01.html')


def culture_project_02(request):
    return render(request, 'pages/culture_project_02.html')


def culture_project_03(request):
    return render(request, 'pages/culture_project_03.html')

def culture_project_04(request):
    return render(request, 'pages/culture_project_04.html')

def culture_project_05(request):
    return render(request, 'pages/culture_project_05.html')
