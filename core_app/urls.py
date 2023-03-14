from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('settings',views.settings,name='settings'),
    path('upload',views.upload,name='upload'),
    path('follow',views.follow,name='follow'),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('user_posts/<str:pk>',views.user_posts,name='user_posts'),
    path('like-post',views.like_post,name='like-post'),
    path('logout',views.logout,name='logout'),
    path('logout',views.logout,name='logout'),
    path('search',views.search,name='search'),
]
