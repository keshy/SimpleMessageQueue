from django.conf.urls import patterns, url

from producer import views

urlpatterns = patterns('',
    url(r'^update/', views.update, name='update')
)
