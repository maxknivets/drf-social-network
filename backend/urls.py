from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework.routers import SimpleRouter

from . import views

app_name = 'backend'

router = SimpleRouter()
router.register(r'api/post', views.PostViewSet)

urlpatterns = [
    # user logging and administration
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('ajax/validate_username/', views.validate_username, name='validate_username'),
    path('admin/', admin.site.urls, name='admin'),
    path('api-auth/', include('rest_framework.urls')),


    path('', include(router.urls)),
    path('api/post/rate/', views.PostRateViewSet.as_view(), name='rate'),
    path('api/post/rating/<int:pk>/', views.PostRateViewSet.as_view(), name='rating'),
    path('api/post/retrieve-comments/<int:pk>/', views.CommentList.as_view(), name='retrieve-comments'),
    
    path('api/profile/', views.ProfileViewSet.as_view(), name='profile-change'),
    path('api/profile/<int:pk>/', views.ProfileViewSet.as_view(), name='profile-retrieve'),
    
    path('api/follow/<int:pk>/', views.follow, name='follow'),
    path('api/following/<int:pk>/', views.Following.as_view(), name='following'),
    path('api/followers/<int:pk>/', views.Followers.as_view(), name='followers'),
]