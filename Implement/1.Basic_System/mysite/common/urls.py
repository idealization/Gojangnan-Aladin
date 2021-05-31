from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='common/signin.html'), name='signin'),
    path('signin/', auth_views.LoginView.as_view(template_name='common/signin.html'), name='signin'),
    path('signup/', views.signup, name='signup'),
]
