from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serailizer import UserSerailzier


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerailzier
    permission_classes = [IsAuthenticated]
