from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .jwt_serializers import LogInTokenObtainPairSerializer, LogOutSerializer


class LogInTokenObtainPairView(TokenObtainPairView):
    serializer_class = LogInTokenObtainPairSerializer

class LogOutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogOutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Logout successful'}, status=status.HTTP_204_NO_CONTENT)
