from django.conf.urls import url

from . import views  # import views so we can use them in urls

urlpatterns = [
    url('^$', views.listing),  # "/store" will call the method "index" in "views.py"
    url(r'^search/$', views.search),
    url(r'^(?P<album_id>[0-9]+)', views.detail)
]
