from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework_jwt.views import obtain_jwt_token

from . import views

app_name = 'social'

urlpatterns = [
    path('token-auth/', obtain_jwt_token),
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
    path('ajax/post/', views.WritePost.as_view(), name='post'),
    path('ajax/retrieveposts/', views.RetrievePosts.as_view(), name='retrieveposts'),
    path('ajax/vote/', views.VoteOnPost.as_view(), name='vote'),
    path('ajax/edit/<int:pk>/', views.Edit.as_view(), name='edit'),
    path('ajax/delete/<int:post_id>/', views.delete, name='delete'),
    path('ajax/comment/', views.WriteComment.as_view(), name='comment'),
    path('ajax/retrievecomments/<int:pk>', views.RetrieveComments.as_view(), name='retrievecomments'),
    path('ajax/commentedit/', views.commentedit, name='commentedit'),
    path('ajax/commentdelete/', views.commentdelete, name='commentdelete'),
    path('ajax/follow/', views.follow, name='follow'),
    path('ajax/settings/', views.settings, name='settings'),
]

