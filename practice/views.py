from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from practice.models import Marker


def map_view(request):
    return render(request, 'practice/map.html', {'markers': Marker.objects.all()})

def save_marker_view(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        message = request.POST.get('message')

        marker = Marker(latitude=latitude, longitude=longitude, message=message)
        marker.save()

    return redirect('map')