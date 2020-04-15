from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """ Create a new user in the system """
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """ Create a new auth token for users. """
    serializer_class = AuthTokenSerializer
    # So we can render the post request from the browser. Otherwise we'd need to use postman to
    # view/test the requests.
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """ Manage the authenticated user. """
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    # We override the get_object so as to only retrieve info about the authenticated user.
    def get_object(self):
        """ Retrieve and return authenticated user. """
        return self.request.user  # user is an attr of the request because we required auth above.
