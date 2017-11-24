'''default api view for remitapi'''
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FormParser
from hotelsApi.authentication import ApiAuthentication
from django.conf import settings
from hotelsApi.v1.serializers import *
from hotelsApi.utils import ApiResponse
from django.views.decorators.csrf import csrf_exempt

from hotelsApi.server import Hotels

import lxml.objectify
from rest_framework.decorators import api_view
from bson.json_util import dumps

import json, ast


class ApiView(APIView):
    """
    Default Api View Class
    """
    authentication_classes = (
        ApiAuthentication,
    )
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (JSONParser, FormParser)




class GetHotels(ApiView):
    """Booking.com Hotels."""
    serializer_class = GetHotelsSerializer

    def post(self, request):
        exception = None
        response = {"result":{"result":None}}
        responsecode = 0
        serializer = self.serializer_class(data=request.data)
        hotels_data = {}
        Message = {}
        ErrorMessage= {}


        if serializer.is_valid():
            print ':Valid serializer'
            hotels = Hotels()

            hotels_data['hotel_ids'] = serializer.validated_data['hotel_ids']
            hotel_ids = hotels_data['hotel_ids']

            print "Hotel id %s" % hotel_ids

            hotels_data['extras'] = serializer.validated_data['extras']
            extras = hotels_data['extras']

            print "Extras id %s" % extras

            hotels_response =hotels.GetHotels(hotel_ids,extras)

            print ':Hotels  View REsponse: ',hotels_response

           
            response['result'] = json.loads(hotels_response)
            print 'Results : %s' % (response)




        else:
            print ':Invalid serializer'
            responsecode = 7
            response['errors'] = serializer.errors

        return ApiResponse(
            responsecode, response, exception
        )






class GetCountries(ApiView):
    """Booking.com countries."""
    

    def post(self, request):
        exception = None
        response = {"result":{"result":None}}
        responsecode = 0
       
        hotels_data = {}
        Message = {}
        ErrorMessage= {}

        print ':Valid serializer'
        hotels = Hotels()

        hotels_response = hotels.GetCountries()

        print ':Hotels  View REsponse: ',hotels_response

       
        response['result'] = json.loads(hotels_response)
        print 'Results : %s' % (response)

    
        return ApiResponse(
            responsecode, response, exception
        )


class GetCities(ApiView):
    """Booking.com countries."""
    

    def post(self, request):
        exception = None
        response = {"result":{"result":None}}
        responsecode = 0
       
        hotels_data = {}
        Message = {}
        ErrorMessage= {}

        print ':Valid serializer'
        hotels = Hotels()

        hotels_response = hotels.GetCountries()

        print ':Hotels  View REsponse: ',hotels_response

       
        response['result'] = json.loads(hotels_response)
        print 'Results : %s' % (response)

    
        return ApiResponse(
            responsecode, response, exception
        )



class GetDistricts(ApiView):
    """Booking.com countries."""
    

    def post(self, request):
        exception = None
        response = {"result":{"result":None}}
        responsecode = 0
       
        hotels_data = {}
        Message = {}
        ErrorMessage= {}

        print ':Valid serializer'
        hotels = Hotels()

        hotels_response = hotels.GetDistricts()

        print ':Hotels  View REsponse: ',hotels_response

       
        response['result'] = json.loads(hotels_response)
        print 'Results : %s' % (response)

    
        return ApiResponse(
            responsecode, response, exception
        )

class GetRegions(ApiView):
    """Booking.com countries."""
    

    def post(self, request):
        exception = None
        response = {"result":{"result":None}}
        responsecode = 0
       
        hotels_data = {}
        Message = {}
        ErrorMessage= {}

        print ':Valid serializer'
        hotels = Hotels()

        hotels_response = hotels.GetRegions(data=None)

        print ':Hotels  View REsponse: ',hotels_response

       
        response['result'] = json.loads(hotels_response)
        print 'Results : %s' % (response)

    
        return ApiResponse(
            responsecode, response, exception
        )



class GetHotelTypes(ApiView):
    """Booking.com Hotels."""
    serializer_class = GetHotelTypesSerializer

    def post(self, request):
        exception = None
        response = {"result":{"result":None}}
        responsecode = 0
        serializer = self.serializer_class(data=request.data)
        hotels_data = {}
        Message = {}
        ErrorMessage= {}


        if serializer.is_valid():
            print ':Valid serializer'
            hotels = Hotels()

            hotels_data['languages'] = serializer.validated_data['languages']
            languages = hotels_data['languages']

            print "Languages %s" % languages

            hotels_data['rows'] = serializer.validated_data['rows']
            rows = hotels_data['rows']

            print "Number of rows%s" % rows

            hotels_response =hotels.GetHotelTypes(languages,rows)

            print ':Hotels  View REsponse: ',hotels_response

           
            response['result'] = json.loads(hotels_response)
            print 'Results : %s' % (response)




        else:
            print ':Invalid serializer'
            responsecode = 7
            response['errors'] = serializer.errors

        return ApiResponse(
            responsecode, response, exception
        )

class GethotelFacilityTypes(ApiView):
    """Booking.com Hotels."""
    serializer_class = GetHotelFacilityTypesSerializer

    def post(self, request):
        exception = None
        response = {"result":{"result":None}}
        responsecode = 0
        serializer = self.serializer_class(data=request.data)
        hotels_data = {}
        Message = {}
        ErrorMessage= {}


        if serializer.is_valid():
            print ':Valid serializer'
            hotels = Hotels()

            hotels_data['languages'] = serializer.validated_data['languages']
            languages = hotels_data['languages']

            print "Languages %s" % languages

            hotels_data['rows'] = serializer.validated_data['rows']
            rows = hotels_data['rows']

            print "Number of rows%s" % rows

            hotels_response =hotels.GetHotelTypes(languages,rows)

            print ':Hotels  View REsponse: ',hotels_response

           
            response['result'] = json.loads(hotels_response)
            print 'Results : %s' % (response)




        else:
            print ':Invalid serializer'
            responsecode = 7
            response['errors'] = serializer.errors

        return ApiResponse(
            responsecode, response, exception
        )
