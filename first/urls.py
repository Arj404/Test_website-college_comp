from django.conf.urls import url
from first import views

urlpatterns = [
    url(r'^$',views.index,name= 'index'),
]