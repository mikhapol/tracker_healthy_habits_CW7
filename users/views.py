from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    Набор представлений для пользовательской модели.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
