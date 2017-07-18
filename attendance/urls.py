from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.admission_list, name='admission_list'),
    url(r'^person/(?P<pk>\d+)/$', views.person_detail, name='person_detail'),
]
