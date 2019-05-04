from django.urls import path
from . import views

app_name = 'oauth'
urlpatterns = [
    path('oauth/login', views.OAuthLoginView.as_view(), name='oauth_login'),

    path('oauth/authorize', views.OAuthAuthorize.as_view(), name='oauth_authorize'),
]
