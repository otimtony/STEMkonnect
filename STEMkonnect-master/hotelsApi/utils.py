from django.conf import settings
import sys
from datetime import datetime
from hotelsApi.response_codes import API_RESPONSE
from django.utils import timezone 
from rest_framework.response import Response
from rest_framework import status
from django.utils.dateformat import format


def ApiResponse(responsecode, response=None, exception=None, statuscode=None):
    '''
    control api response
    '''
    description = ''
    try:
        description = API_RESPONSE[responsecode]
    except Exception, e:
        print e
    if not response:
        response = {}
    response['response'] = description
    response['responsecode'] = responsecode
    response['timestamp'] = format(timezone.now(), 'U')
    if exception and settings.DEBUG_API:
        response['exception'] = exception
    if not statuscode:
        statuscode = status.HTTP_200_OK
    return Response(response, status=statuscode)




def debug(e, txt=False, log='debug'):
    txt = "%s %s" % (e, txt)
    if settings.DEBUG_API:
        if not txt:
            txt = ''
        print >> sys.stderr, 'Debuging____________________ %s' % txt
        print >> sys.stderr, e
    else:
        try:
            old_stdout = sys.stdout
            #log_file = open("%slogs/%s.log" % (settings.LOG_DIR, log), "a")
            log_file = open("%slogs/%s.log" % (settings.BASE_DIR, log), "a")
            sys.stdout = log_file
            print '%s: Debuging_____________%s' % (
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                txt
            )
            print e
            sys.stdout = old_stdout
            log_file.close()
        except Exception, e:
            print e