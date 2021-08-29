from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post,Recommend
from .models import Rating
from .serializers import RatingsSerializer,RecommendSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RatingsViewset(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingsSerializer



@csrf_exempt
def account_list(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RecommendSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
