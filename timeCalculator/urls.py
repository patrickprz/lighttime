from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^calcule/$', views.calcule, name='calcule'),
    #url(r'(?P<result>[a-z])$', views.index, name='indexResult'),
    #url(r'^$', 'index', {'result': 'result'}, name='index'),
]
