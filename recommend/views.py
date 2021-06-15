from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from .models import Rating
from .serializers import RatingsSerializer

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RatingsViewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingsSerializer
