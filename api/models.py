from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Time(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True #设置为抽象基类
        ordering = ['-create_time']

    def __str__(self):
        return self.time

class Movie(Time):
    types = models.IntegerField(verbose_name='类型',null = False)
    title = models.CharField(max_length=255,verbose_name='标题',null = False)
    year = models.IntegerField(verbose_name='年份')
    language = models.CharField(max_length=255,verbose_name='语言')
    poster = models.CharField(max_length=255,verbose_name='海报')
    description = models.TextField(verbose_name='描述')
    ratings = models.FloatField(verbose_name='评分')
    douban_id = models.IntegerField(verbose_name='豆瓣ID')
    actors = models.CharField(max_length=255,verbose_name='演员')
    directors = models.CharField(max_length=255,verbose_name='导演')
    country = models.CharField(max_length=255,verbose_name='国家')

    class Meta:
        db_table = 'movie'
        verbose_name = '电影'
        verbose_name_plural = '电影'
        ordering = ['-create_time']
    
    def __str__(self):
        return self.title



class Category(Time):
    name = models.CharField(max_length=255,verbose_name='分类名称',null = False)
    order = models.IntegerField(verbose_name='分类排序',null = False)

    class Meta:
        db_table = 'category'
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['-create_time']

    def __str__(self):
        return self.name

class Urls(Time):
    status_choices = [
        (0,'无效'),
        (1,'有效'),
    ]
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE,verbose_name='电影ID',null = False)
    url = models.CharField(max_length=255,verbose_name='链接',null = False)
    url_type = models.IntegerField(verbose_name='链接类型',null = False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,verbose_name='分类',null = False)
    status = models.IntegerField(verbose_name='状态',choices=status_choices,default=1)

    class Meta:
        db_table = 'urls'
        verbose_name = '链接'
        verbose_name_plural = '链接'
        ordering = ['-create_time']

    def __str__(self):
        return self.url
    
class Banner(Time):
    status_choices = [
        (0,'无效'), 
        (1,'有效'),
    ]
    movie_id = models.ForeignKey(Movie,on_delete = models.CASCADE,verbose_name='电影ID',null = False)
    status = models.IntegerField(verbose_name='状态',choices=status_choices,default=1)

    class Meta:
        db_table = 'banner'
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'  

    def __str__(self):
        return self.movie_id.title