from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
# url(r'^$', views.index), # This line has changed!
url(r'^$', views.index),
url(r'^users$', views.index),
url(r'^users/new$', views.new_user),
url(r'^users/(?P<id>\d+)$', views.show),
url(r'^users/(?P<id>\d+)/edit$', views.edit),
url(r'^users/(?P<id>\d+)/delete$', views.delete)

]