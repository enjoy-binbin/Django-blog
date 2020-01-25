from django.test import TestCase, Client
from django.urls import reverse

from user.models import UserProfile


# 命令行调用:  python manage.py test app [--keepdb参数: 保留测试数据库, 这样反复测试的时候速度快]
# setting里设置测试数据库的属性
# 会自动执行tests.py下test_开头的测试方法
# 每个的测试方法应该只测试一种情况
# 根据模型或者视图创建测试类

class UserModelTest(TestCase):
    """ 测试User模型 """

    def setUp(self):
        """ 测试方法执行前执行 """
        self.client = Client()

    def test_superuser(self):
        user = UserProfile.objects.create_superuser(username='test_admin', email='admin@qq.com', password='aa123456')

        login_res = self.client.login(username='test_admin', password='aa123456')
        self.assertEqual(login_res, True)  # 上面登陆能成功会返回True

        admin_res = self.client.get(path=reverse('admin:login'))
        self.assertEqual(admin_res.status_code, 302)  # 后台登陆页, 登陆成功会跳转302

        user_res = self.client.get(path=user.get_absolute_url())
        self.assertEqual(user_res.status_code, 200)  # 用户的文章列表

    def test_user(self):
        register_res = self.client.post(path=reverse('user:register'), data={
            "username": 'test_user',
            "email": 'user@qq.com',
            "password1": 'aa123456',
            "password2": 'aa123456',
        })
        self.assertEqual(register_res.status_code, 302)  # 用户注册, 测试的是不需要发邮件激活的
        user = UserProfile.objects.get_or_create(username='test_user')
        self.assertEqual(user[1], False)  # 如果能get到是返回的False

        login_res = self.client.login(username='test_user', password='aa123456')
        self.assertEqual(login_res, True)  # 上面登陆能成功会返回True

        login_res = self.client.post(reverse('user:login'), {
            'username': 'test_user',
            'password': 'aa123456'
        })
        self.assertIn(login_res.status_code, [302])
