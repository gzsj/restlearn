from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Movie,Category,Urls,Banner,types
from .serializers import MovieSerializer,CategorySerializer,UrlsSerializer,BannerSerializer,TypesSerializer
from rest_framework import viewsets

# 电影列表接口
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all() #默认直接返回所有的内容
    serializer_class = MovieSerializer 


# detail 参数决定了该方法是用于单个对象还是多个对象。
    @action(detail=False, methods=['get'], url_path='types/(?P<types_id>\d+)')
    def get_by_types(self, request, types_id):
        movies = Movie.objects.filter(types=types_id)
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)
    
    @action(detail = True, methods = ['get'], url_path = 'poster')
    def get_by_title(self, request, pk=None):
        movie = self.get_object()
        return Response({'poster':movie.poster,'title':movie.title})

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UrlsViewSet(viewsets.ModelViewSet):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class TypesViewSet(viewsets.ModelViewSet):
    queryset = types.objects.all()
    serializer_class = TypesSerializer

