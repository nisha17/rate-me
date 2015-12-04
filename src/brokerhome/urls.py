from django.conf.urls import url,include

from . import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='home'),
    # url(r'^contact/$', views.contact, name='contact'),
   	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='city_details'),
    url(r'^(?P<broker_id>[0-9]+)/rating/$', login_required(views.RatingView.as_view()), name='rating'),
    url(r'^profile/$', views.user_profile, name='profile'),
    # url(r'^locality/$', views.locality_list, name = 'locality'),
    

]
