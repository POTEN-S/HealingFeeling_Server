from rest_framework import serializers # serializer import
from .models import User # 선언한 모델 import

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # 모델 설정
        fields = ('id', 'username', 'age', 'city')  # 필드 설정