from rest_framework.viewsets import ModelViewSet
from userapp.serializers import UserSerializer
from userapp.models import User

class UserAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer