from django.conf.urls import  url
import hotelsApi.v1.views as views


urlpatterns = [

	url(r'^booking/hotels/$',views.GetHotels.as_view()),
	url(r'^booking/countries/$',views.GetCountries.as_view()),
	url(r'^booking/cities/$',views.GetCities.as_view()),
	url(r'^booking/districts/$',views.GetDistricts.as_view()),
	url(r'^booking/regions/$',views.GetRegions.as_view()),
	url(r'^booking/hotelTypes/$',views.GetHotelTypes.as_view()),
	url(r'^booking/hotelFacilityTypes/$',views.GethotelFacilityTypes.as_view()),
]

 


