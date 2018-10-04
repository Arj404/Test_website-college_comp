from django.conf.urls import url
from college import views

urlpatterns = [
    url(r'^$',views.index,name= 'index'),
    url(r'form/',views.form_name,name = 'form'),
]