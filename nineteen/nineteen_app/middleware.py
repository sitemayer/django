
class ShowIP(object):
    def process_request(self, request):
        if  request.META.has_key('HTTP_X_FORWARDED_FOR'):
            request.ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            request.ip = request.META['REMOTE_ADDR']


