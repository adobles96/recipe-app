from rest_framework import generics
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
    