from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm

# Create your views here.
def index(request):
    videos = Video.objects.order_by('-dateAdded')
    context = {'videos': videos}
    return render(request, 'videorequest/index.html', context)

def vrform(request):
    if request.method == "POST":
        form = VideoForm(request.POST)

        if form.is_valid():
            newReq = Video(videoTitle=request.POST['videoName'], videoDescription=request.POST['videoDescription'])
            newReq.save()
            return redirect('index')
    
    else: 
        form = VideoForm()
    
    context = {'form': form}

    return render(request, 'videorequest/vrform.html', context)