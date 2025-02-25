from django.core.management.base import BaseCommand
from api.models import Movie,  types,Urls,Category

class Command(BaseCommand):
    help = "批量插入url数据"

    def handle(self, *args, **kwargs):
        # category = [
        #     Category(name="百度网盘",order=1),
        #     Category(name="阿里网盘",order=2),
        #     Category(name="夸克网盘",order=3),
        #     Category(name="115网盘",order=4),
        #     Category(name="1080P",order=4),
        #     Category(name="720P",order=4),
        #     Category(name="4K",order=4)
        # ]
        
        # Category.objects.bulk_create(category)
        #   `url` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
        #     `status` int NOT NULL,
        #     `category_id` bigint NOT NULL,
        #     `movie_id_id` bigint NOT NULL,
        category = Category.objects.all()
        movies = Movie.objects.all()
        # print(movies.get().id)
        urls = [
            Urls(url="https://www.baidu.com/123",status=1,category_id=category.get(id=1).id,movie_id_id=movies.get(id=1).id),
            Urls(url="https://www.baidu.com/124",status=1,category_id=category.get(id=2).id,movie_id_id=movies.get(id=2).id),
            Urls(url="https://www.baidu.com/125",status=1,category_id=category.get(id=3).id,movie_id_id=movies.get(id=2).id),
            Urls(url="https://www.baidu.com/126",status=1,category_id=category.get(id=4).id,movie_id_id=movies.get(id=1).id),
            Urls(url="https://www.baidu.com/127",status=1,category_id=category.get(id=5).id,movie_id_id=movies.get(id=3).id),
            Urls(url="https://www.baidu.com/128",status=1,category_id=category.get(id=6).id,movie_id_id=movies.get(id=3).id),
            Urls(url="https://www.baidu.com/129",status=1,category_id=category.get(id=1).id,movie_id_id=movies.get(id=1).id),
        ]
        Urls.objects.bulk_create(urls)
        self.stdout.write(self.style.SUCCESS("✅ 批量插入成功！"))
