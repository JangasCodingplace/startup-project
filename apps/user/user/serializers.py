from rest_framework import serializers


class UserIsTakenSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
