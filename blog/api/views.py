from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,  # 搜索过滤器 ?search=value
    OrderingFilter,  # 排序过滤器 ?ordering=key
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    # UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    # DestroyAPIView,
)
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import (
    # is_staff = True
    IsAuthenticatedOrReadOnly,  # 登陆用户，或者未登录用户是只读
    AllowAny,
    IsAuthenticated
)

from blog.models import Article, Category
from .pagination import ArticlePageNumberPagination
from .permissions import IsSuperUser, IsAuthor, IsAuthorOrReadOnly
from .serializers import (
    ArticleListSerializer,
    ArticleCreateSerializer,
    ArticleDetailSerializer,
    ArticleUpdateSerializer,
    CategorySerializer,
    CategoryDetailSerializer,
)


class ArticleListAPIView(ListAPIView):
    """ 博客文章列表Api """

    serializer_class = ArticleListSerializer
    filter_backends = [SearchFilter, OrderingFilter]  # OrderingFilter排序 ordering=key
    search_fields = ['title', 'content', 'author__username']  # 可搜索的字段 search=value
    pagination_class = ArticlePageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):  # 不重写默认是返回 self.queryset
        queryset = Article.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(  # i 忽略大小写
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(author__username__icontains=query)
            )

        return queryset


class ArticleCreateAPIView(CreateAPIView):
    """ 博客文章创建Api """

    serializer_class = ArticleCreateSerializer
    permission_classes = [IsSuperUser]  # 超级用户才能创建文章

    def perform_create(self, serializer):
        # 修改作者为当前登陆用户
        serializer.save(author=self.request.user)


class ArticleEditAPIView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
    """ 文章更新编辑、删除API """
    queryset = Article.objects.all()
    lookup_url_kwarg = 'article_id'
    serializer_class = ArticleDetailSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryListAPIView(ListAPIView):
    """ 分类列表Api """
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = ArticlePageNumberPagination

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset


class CategoryDetailAPIView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
    """ 分类详情Api """
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    lookup_url_kwarg = 'category_id'
    lookup_field = 'id'
    permission_classes = [AllowAny]  # 超级用户才能创建文章分类

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryCreateAPIView(CreateAPIView):
    """ 分类创建API """
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUser]


class ArticleDetailAPIView(RetrieveAPIView):
    """ 博客文章详情APi，都可以整合到ArticleEditAPIView """

    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'id'  # 查找的字段, 默认为pk 主键
    lookup_url_kwarg = 'article_id'  # urls里的参数, 默认会等于 lookup_field
    permission_classes = [IsAuthenticatedOrReadOnly]


class ArticleUpdateAPIView(RetrieveUpdateDestroyAPIView):
    """ 博客文章更新APi, 都可以整合到ArticleEditAPIView """

    queryset = Article.objects.all()
    serializer_class = ArticleUpdateSerializer
    lookup_url_kwarg = 'article_id'
    permission_classes = [IsAuthor]
