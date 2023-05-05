from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

class CustomTokenAuthenticationTest(authentication.BaseAuthentication):
    def authenticate(self, request):


        #username = request.META.get('HTTP_X_USERNAME')
        #if not username:
        #    return None
        user = None
        try:
            headers = request.headers
            if 'Authorization' in headers:
                if headers['Authorization'] == 'Bearer aqsdcvawevbavas':
                    user = User.objects.get(username='admin')
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)