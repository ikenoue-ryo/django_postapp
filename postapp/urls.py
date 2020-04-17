from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'postapp'

urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('new/', login_required(views.New.as_view()), name='new'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
]
