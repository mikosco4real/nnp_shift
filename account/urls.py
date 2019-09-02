from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from .views import Register

app_name = "account"

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name="account/login.html", authentication_form=LoginForm), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
    path('register', Register.as_view(), name='register')
]
