from django.conf.urls import url
from . import views

urlpatterns = [
# ex: /
url(r'^$', views.home, name='home'),
# ex: /5/
url(r'^(?P<indizio_id>[0-9]+)/$', \
	views.indizio, name='indizio'),
	#url(r'^fine$', views.end, name='end'),
] 