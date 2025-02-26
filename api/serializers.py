from rest_framework import serializers
from .models import Movie, Category, Urls, Banner, types

class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = types
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    # types = TypesSerializer()
    class Meta:
        model = Movie
        fields = ['id','types', 'title', 'poster', 'description']



#专属于url movie关联的序列化
class UrlsMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UrlsSerializer(serializers.ModelSerializer):
    movie = UrlsMovieSerializer(source='movie_id')
    
    class Meta:
        model = Urls
        fields = ['movie','url','category','status']
        # depth = 1

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        depth = 1