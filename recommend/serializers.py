from rest_framework import  serializers
from .models import Post, Recommend
from .models import Rating

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('ratings','title','bookratings','booktitle','whereratings','wheretitle')


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('ratings','title','bookratings','booktitle','whereratings','wheretitle')


class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = ('userId','emotion','category')