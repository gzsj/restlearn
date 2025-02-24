from rest_framework import serializers
from .models import Movie, Category, Urls, Banner

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urls
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'