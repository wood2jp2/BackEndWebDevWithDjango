from django.shortcuts import render
from .models import Video

# Create your views here.
def index(request):
    videos = Video.objects.order_by('-dateAdded')
    context = {'videos': videos}
    return render(request, 'videorequest/index.html', context)

def vrform(request):
    return render(request, 'videorequest/vrform.html')