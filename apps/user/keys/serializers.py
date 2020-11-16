from rest_framework import serializers
from user.user.models import User
from .models import Key


class CreateKeySerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True, required=True)

    def get_user(self, email):
        try:
            return User.objects.get(emai=email)
        except User.DoesNotExist:
            return None

    def create(self, validated_data):
        user = self.get_user(validated_data['email'])
        if user:
            Key.objects.create(user=user)
        return {}
