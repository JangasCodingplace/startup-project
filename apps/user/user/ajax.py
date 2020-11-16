from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserIsTakenSerializer


class UserIsTakenAPI(APIView):
    def get_queryset(self, email):
        queryset = User.objects.filter(email=email)
        return queryset.exists()

    def get(self, request, *args, **kwargs):
        email = request.query_params.get('email')
        UserIsTakenSerializer(data={'email': email})
        user_is_taken = self.get_queryset(email)
        return Response({'user_is_taken': user_is_taken},
                        status=status.HTTP_200_OK)
