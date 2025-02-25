# 在 tests.py
from django.test import TestCase
from .models import Movie  # 确保导入正确的模型

class MovieTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """ 预先创建类型数据，并插入多个电影测试数据 """

        movies = [
            Movie(
                types=1, title="好东西", year=2010, language="English",
                poster="https://example.com/inception.jpg", description="A mind-bending thriller",
                ratings=8.8, douban_id=12345, actors="Leonardo DiCaprio", directors="Christopher Nolan",
                country="USA"
            ),
            Movie(
                types=2, title="乡村爱情", year=2014, language="English",
                poster="https://example.com/interstellar.jpg", description="A space exploration epic",
                ratings=8.6, douban_id=67890, actors="Matthew McConaughey", directors="Christopher Nolan",
                country="USA"
            ),
            Movie(
                types=3, title="再见爱人", year=2012, language="English",
                poster="https://example.com/django.jpg", description="A Tarantino classic",
                ratings=8.4, douban_id=13579, actors="Jamie Foxx", directors="Quentin Tarantino",
                country="USA"
            ),
        ]

        Movie.objects.bulk_create(movies)  # 批量插入数据

    def test_movie_count(self):
        """ 确保 3 条数据正确插入 """
        self.assertEqual(Movie.objects.count(), 3)

# types = models.ForeignKey(types,on_delete=models.CASCADE,verbose_name='类型',null = False)
#     title = models.CharField(max_length=255,verbose_name='标题',null = False)
#     year = models.IntegerField(verbose_name='年份')
#     language = models.CharField(max_length=255,verbose_name='语言')
#     poster = models.CharField(max_length=255,verbose_name='海报')
#     description = models.TextField(verbose_name='描述')
#     ratings = models.FloatField(verbose_name='评分')
#     douban_id = models.IntegerField(verbose_name='豆瓣ID')
#     actors = models.CharField(max_length=255,verbose_name='演员')
#     directors = models.CharField(max_length=255,verbose_name='导演')
#     country = models.CharField(max_length=255,verbose_name='国家')