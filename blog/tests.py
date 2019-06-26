from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from blog.models import Category, Article, Comment

User = get_user_model()


# 命令行调用:  python manage.py test app [--keepdb参数: 保留测试数据库, 这样反复测试的时候速度快]
# setting里设置测试数据库的属性
# 会自动执行tests.py下test_开头的测试方法
# 每个的测试方法应该只测试一种情况
# 根据模型或者视图创建测试类


class ArticleModelTest(TestCase):
    def setUp(self):
        self.client = Client()  # 普通客户端
        self.client_user = Client()  # 普通用户登录用的客户端
        self.client_superuser = Client()  # 管理员登录用的客服端
        self.superuser = User.objects.create_superuser('test_admin', 'admin@qq.com', 'aa123456')
        self.user = User.objects.create_user('test_user', 'user@qq.com', 'aa123456')

        self.client_user.login(username='test_user', password='aa123456')
        self.client_superuser.login(username='test_admin', password='aa123456')

        self.category = Category.objects.create(name='test_category')
        self.article = Article.objects.create(category=self.category, author=self.superuser,
                                              title='test_article', content='test_article_content')

    def test_category(self):
        category_res = self.client.get(self.category.get_absolute_url())
        self.assertEqual(category_res.status_code, 200)

    def test_article(self):
        # 这里就简单的测试创建5篇文章
        for i in range(1, 6):
            article = Article()
            article.category = self.category
            article.author = self.superuser
            article.title = 'title' + str(i)
            article.content = 'content' + str(i)
            article.save()

        self.assertEqual(len(Article.objects.all()), 5 + 1)
        article_detail_res = self.client.get(Article.objects.first().get_absolute_url())
        self.assertEqual(article_detail_res.status_code, 200)

    def test_comment(self):
        comment_url = reverse('blog:comment', kwargs={'article_id': self.article.id})
        comment_res = self.client_user.post(comment_url, data={'content': 'test_comment'})

        self.assertEqual(Comment.objects.first().content, 'test_comment')
        self.assertEqual(comment_res.status_code, 302)

    def test_page404(self):
        page404_res = self.client.get('/彬彬冲呀66666666')
        self.assertEqual(page404_res.status_code, 404)

        page404_res = self.client.get('/refresh')
        self.assertEqual(page404_res.status_code, 301)  # 未登录用户访问会先跳转到登录页

    def test_refresh(self):
        # 301永久重定向, 客户端可以对结果进行缓存, 当访问原地址会直接进行本地302跳转, 两次请求先一次301再一次302
        # 302临时重定向, 客户端必须请求原链接
        page301_res = self.client_superuser.get('/refresh')  # '/', 这个会先进行301, 然后在302
        page302_res = self.client_superuser.get('/refresh/')  # 管理员refresh后会302到首页
        self.assertEqual(page301_res.status_code, 301)
        self.assertEqual(page302_res.status_code, 302)

        page403_res = self.client_user.get('/refresh/')  # 这里需要加'/', 不然会先进行301的
        self.assertEqual(page403_res.status_code, 403)  # 普通用户访问是403, 没有权限

        page302_res = self.client.get('/refresh/')
        self.assertEqual(page302_res.status_code, 302)  # 未登录访问302到登录页

    def test_feed_and_sitemap(self):
        feed_res = self.client.get('/feed/')  # /feed是301, 需要跟url里的匹配
        self.assertEqual(feed_res.status_code, 200)

        sitemap_res = self.client.get('/sitemap.xml')
        self.assertEqual(sitemap_res.status_code, 200)
