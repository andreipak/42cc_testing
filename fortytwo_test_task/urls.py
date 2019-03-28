from django.conf.urls import url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # http://sjoerdjob.com/post/reusing-django-include-urls-for-index/
    url(r'^', include('apps.hello.urls', namespace='hello'), name='index'),
    url(r'^admin/', admin.site.urls),
]
