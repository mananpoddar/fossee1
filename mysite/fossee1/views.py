from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from fossee1.models import Caption,Images
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


ini =0

#for front page
def index(request):
    return render(request,"fossee1/index.html")

#handle uploading images
@csrf_exempt
def uploadImage(request):
    if request.method=="POST":
        ini =0
        if ini == 0:
                caption = Caption(
                title = request.POST.get('title'),
                description = request.POST.get('description')
                )
                caption.save()
                ini =1
        image = Images(
            image = request.FILES.get('image')

        )
        image.save()
        
    return render(request,"fossee1/uploadImage.html")

#handle rendering images
def viewImage(request):
    print("viewImage")
    caption = Caption.objects.all()[0]
    image = Images.objects.all()
    return render(request,"fossee1/viewImage.html",{"caption":caption,"image":image})