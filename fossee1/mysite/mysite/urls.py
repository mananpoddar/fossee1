from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^fossee1/', include("fossee1.urls" , namespace="fossee1")),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
