''' ipay '''
import stemconnect.settings as settings
from hotelsApi.utils import debug
import requests
import hashlib
import time
import json
from django.utils import timezone 
from suds.client import Client

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
headers = settings.headers
from requests.auth import HTTPBasicAuth

class Hotels():

    def __init__(self):
        self.settings = settings

   

    
    def GetHotels(self, hotel_ids,extras):
        
        endpoint = settings.HOTELS_URL
        url = 'hotels?'

        params = {}
        response = {}

        hotel_ids = hotel_ids
        extras = extras

        print "Extras id %s" % extras
       

        url = "https://distribution-xml.booking.com/2.0/json/hotels?hotel_ids=%s&extras=%s" % (hotel_ids,extras)
        # instr = "'{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}'".format(softname, procversion, int(percent), exe, description, company, procurl)
        
        debug(url, 'processing Booking payload', 'Booking')
        try:
            r = requests.post(url, auth=HTTPBasicAuth('booking_hackathon_uganda', 'UgandaH4ckerz'))
            response = r.text

            print "Response %s" % (response)
        except Exception, e:
            debug(e, 'error processing Booking', 'Booking')
            response['error'] = e
        return response



    def GetCountries(self):

        endpoint = settings.HOTELS_URL
        url = 'countries'
       
        url = "%s%s" % (
                endpoint,
                url,
            )
        debug(url, 'processing Booking payload', 'Booking')
        try:
            r = requests.post(url, auth=HTTPBasicAuth('booking_hackathon_uganda', 'UgandaH4ckerz'))
            response = r.text

            print "Response %s" % (response)
        except Exception, e:
            debug(e, 'error processing Booking', 'Booking')
            response['error'] = e
        return response

    def GetCities(self):

        endpoint = settings.HOTELS_URL
        url = 'cities'
       
        url = "%s%s" % (
                endpoint,
                url,
            )
        debug(url, 'processing Booking payload', 'Booking')
        try:
            r = requests.post(url, auth=HTTPBasicAuth('booking_hackathon_uganda', 'UgandaH4ckerz'))
            response = r.text

            print "Response %s" % (response)
        except Exception, e:
            debug(e, 'error processing Booking', 'Booking')
            response['error'] = e
        return response
        


    def GetDistricts(self):

        endpoint = settings.HOTELS_URL
        url = 'districts'
       
        url = "%s%s" % (
                endpoint,
                url,
            )
        debug(url, 'processing Booking payload', 'Booking')
        try:
            r = requests.post(url, auth=HTTPBasicAuth('booking_hackathon_uganda', 'UgandaH4ckerz'))
            response = r.text

            print "Response %s" % (response)
        except Exception, e:
            debug(e, 'error processing Booking', 'Booking')
            response['error'] = e
        return response


    def GetRegions(self, data=None):

        endpoint = settings.HOTELS_URL
        url = 'regions'
       
        url = "%s%s" % (
                endpoint,
                url,
            )
        debug(url, 'processing Booking payload', 'Booking')
        try:
            r = requests.post(url, auth=HTTPBasicAuth('booking_hackathon_uganda', 'UgandaH4ckerz'))
            response = r.text

            print "Response %s" % (response)
        except Exception, e:
            debug(e, 'error processing Booking', 'Booking')
            response['error'] = e
        return response



    def GetHotelTypes(self, languages,rows):
        
        endpoint = settings.HOTELS_URL
        url = 'hotelTypes?'

        params = {}
        response = {}

        languages = languages
        rows = rows

        print "no rows %s" % rows

        url = "https://distribution-xml.booking.com/2.0/json/hotelTypes?languages=%s&rows=%s" % (languages,rows)
        # instr = "'{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}'".format(softname, procversion, int(percent), exe, description, company, procurl)
        
        debug(url, 'processing Booking payload', 'Booking')
        try:
            r = requests.post(url, auth=headers)
            response = r.text

            print "Response %s" % (response)
        except Exception, e:
            debug(e, 'error processing Booking', 'Booking')
            response['error'] = e
        return response

        

        