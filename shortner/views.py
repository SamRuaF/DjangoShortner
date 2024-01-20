from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')



def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        newUrl = Url(link = link, uuid = uid)
        newUrl.save()
        return HttpResponse(uid)
    
def go(request, pk):
    urldetails = Url.objects.get(uuid=pk)
    if not (urldetails.link.startswith("http://") or urldetails.link.startswith("https://")):
        urldetails.link = "https://" + urldetails.link
    return redirect(urldetails.link)
