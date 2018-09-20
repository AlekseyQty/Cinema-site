from django.conf.urls import url

from . import views

app_name = 'cinema'
urlpatterns = [
    url(r'^$', views.IndexView,name = 'index'),
    url(r'^(?P<pk>[0-9]+)/$', views.SessionView,name = 'session'),
    url(r'^([0-9]+)/(?P<pk>[0-9]+)/$', views.DetailView, name='detail'),
    url(r'^checkout/(?P<pk>[0-9]+)$', views.PurchaseView,name = 'index'),
    url(r'^checkout/[0-9]+/success$', views.EndView,name = 'index1'),
]