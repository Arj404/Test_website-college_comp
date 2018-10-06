from django.conf.urls import url
from forms import views

urlpatterns = [
    url(r'^$', views.form_name ,name = 'form'),
    url(r'user/',views.users,name = 'form')
]