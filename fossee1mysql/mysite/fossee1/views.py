from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from fossee1.models import Caption,Images
ini =0
# Create your views here.
@csrf_exempt
def index(request):
    if request.method=="POST":
        ini =0
        if ini == 0:
                i = Images.objects.all()
                print(i)
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
    return render(request,"fossee1/index.html")