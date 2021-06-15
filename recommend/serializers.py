from rest_framework import  serializers
from .models import Post
from .models import Rating

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','text')


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('ratings','title')