from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'postapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new/', views.New.as_view(), name='new'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
