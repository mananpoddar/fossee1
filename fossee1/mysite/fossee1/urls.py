from django.conf.urls import url
from django.conf.urls.static import static
from fossee1 import views
app_name = "fossee1"

urlpatterns = [
    url(r'^$', views.index, name='index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)