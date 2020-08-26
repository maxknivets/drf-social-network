from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views
from rest_framework.authtoken import views as rest_auth_views

app_name = 'backend'

urlpatterns = [
    # stuff for queries
    path('api-token-auth/', rest_auth_views.obtain_auth_token, name='api-token-auth'),

    # user logging and administration
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('ajax/validate_username/', views.validate_username, name='validate_username'),
    path('admin/', admin.site.urls, name='admin'),

    # user info pages and actions
    path('user/<int:user_id>/', views.user, name='user'),
    path('following/<int:user_id>/', views.following, name='following'),
    path('followers/<int:user_id>/', views.followers, name='followers'),
    path('ajax/follow/', views.follow, name='follow'),

    # user settings
    path('ajax/settings/', views.changeinfo, name='settings'),

    # posts
    path('api/post/', views.PostDetail.as_view(), name='post-details'),
    path('api/post/get/<int:pk>/', views.PostGet.as_view(), name='get-post'),
    path('api/post/edit/<int:pk>/', views.PostDetail.as_view(), name='edit-post'),
    path('api/post/delete/<int:pk>/', views.PostDetail.as_view(), name='delete-post'),
    path('api/post/rate/', views.RatePost.as_view(), name='rate-post'),
    path('api/post/rating/<int:pk>/', views.PostRating.as_view(), name='rating'),
    path('api/post/retrieve-posts/', views.PostList.as_view(), name='retrieve-posts'),
    path('api/post/retrieve-comments/<int:pk>/', views.CommentList.as_view(), name='retrieve-comments'),
    path('api/post/comment-count/<int:pk>/', views.CommentCount.as_view(), name='comment-count'),
]

"""
    # comment-related actions
    path('ajax/comment/', views.WriteComment.as_view(), name='comment'),
    path('ajax/commentedit/', views.commentedit, name='comment_edit'),
    path('ajax/commentdelete/', views.commentdelete, name='comment_delete'),
    path('api/comment/count/<int:post_id>/', views.CommentCount.as_view(), name='comment-count'),
    #path('<int:comment_id>/showcomment/', views.showcomment, name='show_comment'),
"""
