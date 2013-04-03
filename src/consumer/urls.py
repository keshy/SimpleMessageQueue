from django.conf.urls import patterns, url

from consumer import views

urlpatterns = patterns('',
    url(r'^consume/', views.consume, name='consume')
)
