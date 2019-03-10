from django.conf.urls import url
from fossee1 import views
app_name = "fossee1"

urlpatterns = [
    url(r'^$', views.index, name='index'),
]