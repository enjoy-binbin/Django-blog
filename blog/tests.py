from django.test import TestCase, Client

from user.models import UserProfile
from blog.models import Category, Article


# 命令行调用:  python manage.py test app [--keepdb参数: 保留测试数据库, 这样反复测试的时候速度快]
# setting里设置测试数据库的属性
# 会自动执行tests.py下test_开头的测试方法
# 每个的测试方法应该只测试一种情况
# 根据模型或者视图创建测试类


class ArticleModelTest(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create_superuser('test_admin', 'admin@qq.com', 'aa123456')
        self.category = Category.objects.create(name='category')
        self.client = Client()

    def test_article(self):
        # 这里就简单的测试创建5篇文章
        for i in range(1, 6):
            article = Article()
            article.category = self.category
            article.author = self.user
            article.title = 'title' + str(i)
            article.content = 'content' + str(i)
            article.save()

        self.assertEqual(len(Article.objects.all()), 5)
        article_detail_res = self.client.get(Article.objects.first().get_absolute_url())
        self.assertEqual(article_detail_res.status_code, 200)
        # 测试用例是真的可以写很多呀...
