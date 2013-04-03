from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SimpleMessageQueue.views.home', name='home'),
    # url(r'^SimpleMessageQueue/', include('SimpleMessageQueue.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    # URL mapper for producer URL
    url(r'^producer/', include('producer.urls')),
    
    url(r'^consumer/', include('consumer.urls'))
)
