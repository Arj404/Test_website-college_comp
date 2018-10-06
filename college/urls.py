from django.conf.urls import url
from college import views

urlpatterns = [
    url(r'^$',views.index,name= 'index'),

]