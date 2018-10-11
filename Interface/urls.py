from django.conf.urls import url
from django.urls import path

from . import views
from .views import *

app_name = 'Interface'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^index/$', views.index, name='index'),
    # url(r'^about/$', views.about, name='about'),
    # url(r'^tours/$', views.tours, name='tours'),
    # url(r'^contact/$', views.contact, name='contact'),
    # url(r'^info/$', views.info, name='info'),
    # path('city/<int:city_id>/', views.city, name='city'),
    url(r'^$', view=ImageView.as_view(), name='base'),
    # path('trip/form/<int:trip_id>/', view=TripFormView.as_view(), name='form'),
    # path('form/<int:hotel_id>/', view=HotelFormView.as_view(), name='form'),
    # path('hotel_detail/<str:hotel_name>/', views.hotel_detail, name='hotel_detail'),
    # path('trip_detail/<int:trip_id>/', views.trip_detail, name='trip_detail'),
]