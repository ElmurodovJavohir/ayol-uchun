from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serailizer import UserSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
