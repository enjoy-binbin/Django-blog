from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # 文章日期归档
    path('archives.html', views.ArchivesView.as_view(), name='archives'),

    # 单个文章详情
    path('article/<int:article_id>/<str:title>.html', views.ArticleDetailView.as_view(), name='article_detail'),

    # 分类下的所有文章列表，可以使用slug作为url 或者 像文章一样用 title
    path('category/<slug:slug>.html', views.CategoryArticleView.as_view(), name='category_article'),

    # 标签下的所有文章列表
    path('tag/<int:tag_id>/<str:name>.html', views.TagArticleView.as_view(), name='tag_article'),

    # 作者下的所有文章列表
    path('author/<str:author_name>.html', views.AuthorArticleView.as_view(), name='author_article'),

    # 评论
    path('article/<int:article_id>/postcomment', views.CommentPostView.as_view(),name='comment')

]
