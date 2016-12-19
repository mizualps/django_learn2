from django.conf.urls import url
from upload_form import views

urlpatterns = [
    url(r'(?P<id>\d+)/$', views.lookBy, name = 'form'),
    url(r'^upload_page/', views.form, name = 'form'),
    url(r'^complete/', views.complete, name = 'complete'),
]