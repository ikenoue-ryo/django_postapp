from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'postapp'

urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('new/', login_required(views.New.as_view()), name='new'),
    path('edit/<int:pk>/', login_required(views.Edit.as_view()), name='edit'),
    path('delete/<int:pk>/', login_required(views.Delete.as_view()), name='delete'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/<int:pk>/', login_required(views.ProfileView.as_view()), name='profile'),
    path('profile/edit/<int:pk>/', login_required(views.ProfileEditView.as_view()), name='profile_edit'),
    path('<postId>/like/', login_required(views.Likes.as_view()), name='like'),
    path('<postId>/comment/', login_required(views.AddComment.as_view()), name='comment'),
    path('delete/comment/<int:pk>/', login_required(views.DeleteComment.as_view()), name='delete_comment'),
    path('tag/<int:pk>', views.Tag.as_view(), name='tag'),
]
