from django.shortcuts import render
from .models import Movie,Category,Urls,Banner,types
from .serializers import MovieSerializer,CategorySerializer,UrlsSerializer,BannerSerializer,TypesSerializer
from rest_framework import viewsets


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

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

