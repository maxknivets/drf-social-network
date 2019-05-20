from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

app_name = 'social'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('admin/', admin.site.urls, name='admin'),
    path('user/<int:user_id>/', views.user, name='user'),
    path('following/<int:user_id>/', views.following, name='following'),
    path('followers/<int:user_id>/', views.followers, name='followers'),
    path('changepfp/', views.changepfp, name='changepfp'),
    path('', views.index, name='index'),
    path('<int:comment_id>/showcomment/', views.showcomment, name='showcomment'),
    path('ajax/validate_username/', views.validate_username, name='validate_username'),
    path('ajax/post/', views.post, name='post'),
    path('ajax/databasecheck/<int:post_id>/', views.databasecheck, name='databasecheck'),
    path('ajax/commentdatabasecheck/<int:comment_id>/', views.commentdatabasecheck, name='commentdatabasecheck'),
    path('ajax/getpostinfo/<int:pk>/', views.GetPostInfo.as_view(), name='getpostinfo'),
    path('ajax/getcommentinfo/<int:comment_id>/', views.getcommentinfo, name='getcommentinfo'),
    path('ajax/vote/<slug:vote>/<int:post_id>/', views.vote, name='vote'),
    path('ajax/edit/', views.edit, name='edit'),
    path('ajax/delete/', views.delete, name='delete'),
    path('ajax/comment/', views.comment, name='comment'),
    path('ajax/commentedit/', views.commentedit, name='commentedit'),
    path('ajax/commentdelete/', views.commentdelete, name='commentdelete'),
    path('ajax/follow/', views.follow, name='follow'),
    path('ajax/settings/', views.settings, name='settings'),
]

