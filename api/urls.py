from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Movie, Category, Urls, Banner,types
from .views import MovieViewSet, CategoryViewSet, UrlsViewSet, BannerViewSet, TypesViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'urls', UrlsViewSet)
router.register(r'banners', BannerViewSet)
router.register(r'types', TypesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]