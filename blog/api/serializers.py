from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)

from blog.models import Article, Category
from user.models import UserProfile


# NOTE: 在drf中用 serializer代替 django.form
# serializer针对json，form针对html
class CategorySerializer(ModelSerializer):
    """ 文章分类序列化 """

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'parent_category']
        extra_kwargs = {'slug': {'read_only': True}}


class CategoryChildSerializer(ModelSerializer):
    """ 分类子类序列化 """

    class Meta:
        model = Category
        fields = ['id', 'name']


class CategoryDetailSerializer(ModelSerializer):
    """ 分类详情序列化 """
    article_count = SerializerMethodField()  # 分类下的文章数
    children = SerializerMethodField()  # 子分类
    articles = SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent_category', 'article_count', 'children', 'articles']

    def get_article_count(self, obj):
        return Article.objects.filter(category=obj).count()

    def get_children(self, obj):
        children = Category.objects.filter(parent_category=obj)
        return CategoryChildSerializer(children, many=True).data or None

    def get_articles(self, obj):
        articles = Article.objects.filter(category=obj)  # 找到当前分类下的所有文章
        # 对文章进行序列化, 外键需要设置 many=True, 因为 文章序列化里用到HyperlinkedIdentityField, 所以需要加request
        articles = ArticleDetailSerializer(articles, many=True, context={'request': self.context['request']}).data
        return articles


class AuthorSerializer(ModelSerializer):
    """ 文章作者序列化 """

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'nickname', 'gender']


class ArticleListSerializer(ModelSerializer):
    """ 文章列表序列化 """
    category = SerializerMethodField()  # 会找到 get_key方法 获取返回值
    author = SerializerMethodField()
    url = HyperlinkedIdentityField(
        view_name='api-blog:article_detail',
        lookup_field='id',
        lookup_url_kwarg='article_id'
    )  # 文章详情页url

    class Meta:
        model = Article
        fields = ['url', 'id', 'category', 'author', 'title', 'content']  # '__all__'

    def get_author(self, obj):
        return obj.author.username

    def get_category(self, obj):
        return obj.category.name


class ArticleCreateSerializer(ModelSerializer):
    """ 文章创建序列化 """

    class Meta:
        model = Article
        fields = ['category', 'title', 'content', 'tags']


class ArticleDetailSerializer(ModelSerializer):
    """ 文章详情序列化 """
    url = HyperlinkedIdentityField(
        view_name='api-blog:article_detail',
        lookup_field='id',
        lookup_url_kwarg='article_id'
    )
    category = CategorySerializer(read_only=True)  # 嵌套序列化
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['url', 'category', 'author', 'title', 'content', 'views']
        read_only_fields = ['views']


class ArticleUpdateSerializer(ModelSerializer):
    """ 文章修改序列化 """
    category = CategorySerializer()

    class Meta:
        model = Article
        fields = ['category', 'title', 'content', 'views']
