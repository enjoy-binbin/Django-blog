from django.urls import path

from . import views

app_name = 'api-blog'

# TODO：想想看这个怎么继续分层

urlpatterns = [
    path('article/', views.ArticleListAPIView.as_view(), name='article_list'),
    path('article/create/', views.ArticleCreateAPIView.as_view(), name='article_create'),
    path('article/<int:article_id>/', views.ArticleEditAPIView.as_view(), name='article_detail'),
    path('article/<int:article_id>/edit/', views.ArticleEditAPIView.as_view(), name='article_edit'),

    path('category/', views.CategoryListAPIView.as_view(), name='category_list'),
    path('category/create/', views.CategoryCreateAPIView.as_view(), name='category_create'),
    path('category/<int:category_id>/', views.CategoryDetailAPIView.as_view(), name='category_detail'),
]
