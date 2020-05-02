from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'postapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new/', login_required(views.New.as_view()), name='new'),
    path('edit/<int:pk>/', login_required(views.Edit.as_view()), name='edit'),
    path('delete/<int:pk>/', login_required(views.Delete.as_view()), name='delete'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/<slug:profname>/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/<slug:profname>/', login_required(views.ProfileEditView.as_view()), name='profile_edit'),
    path('<slug:profname>/follow', views.follow_view, name='follow'),
    path('<slug:profname>/unfollow', views.unfollow_view, name='unfollow'),
    path('<postId>/like/', login_required(views.Likes.as_view()), name='like'),
    path('<postId>/comment/', login_required(views.AddComment.as_view()), name='comment'),
    path('delete/comment/<int:pk>/', login_required(views.DeleteComment.as_view()), name='delete_comment'),
    path('tag/<int:pk>', views.Tag.as_view(), name='tag'),
]
