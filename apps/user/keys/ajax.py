from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CreateKeySerializer


class CreateKeyAPI(APIView):
    def post(self, request, *args, **kwargs):
        key = CreateKeySerializer(data=request.data)
        key.is_valid(raise_exception=True)
        key.save()
        return Response({}, status=status.HTTP_200_OK)
