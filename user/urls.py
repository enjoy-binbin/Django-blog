from django.urls import path, re_path

from . import views
from .forms import LoginForm

app_name = 'user'

urlpatterns = [
    path('login/', views.LoginView.as_view(success_url='/'), name='login', kwargs={'authentication_form': LoginForm}),
    path('register/', views.RegisterView.as_view(success_url="/"), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('active/<code>', views.ActiveView.as_view(), name='active'),
]
