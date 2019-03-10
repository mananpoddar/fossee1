from django.contrib import admin
from django.conf.urls import url, include
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^fossee1/', include("fossee1.urls" , namespace="fossee1")),



]
