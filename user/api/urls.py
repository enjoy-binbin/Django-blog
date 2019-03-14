from django.urls import path

from . import views

app_name = 'api-user'

urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('register/', views.UserCreateAPIView.as_view(), name='register'),
]
