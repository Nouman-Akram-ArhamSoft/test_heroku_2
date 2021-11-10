from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect


class UserRestrictionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        paths = ['/todoproject/', '/todoproject/login/', '/todoproject/registration/']

        if str(user) != 'AnonymousUser' or (request.path.strip() in paths):
            response = self.get_response(request)
            return response
        else:
            return HttpResponse("<h1>Please Login First</h1>")

