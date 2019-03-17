from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from fossee1.models import Caption,Images
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse



# argument: request 
# what it does:renders the front page 
# returns: returns the front page
def index(request):
    return render(request,"fossee1/index.html")

# argument: request 
# what it does:get's the file from user one by one through ajax requests,
#              saves it in the database.
# returns: returns the page where user can upload the Images
@csrf_exempt
def uploadImage(request):
    if request.method=="POST":
        
        caption = Caption(
        title = request.POST.get('title'),
        description = request.POST.get('description')
        )
        caption.save()
        image = Images(
            image = request.FILES.get('image')

        )
        image.save()
        
    return render(request,"fossee1/uploadImage.html")

# argument: request 
# what it does:gets all the documents from the database
# returns: returns the page rendering all the Images
def viewImage(request):
    print("viewImage")
    caption = Caption.objects.all()[0]
    image = Images.objects.all()
    return render(request,"fossee1/viewImage.html",{"caption":caption,"image":image})