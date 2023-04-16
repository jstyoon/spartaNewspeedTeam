from django.urls import path
from . import views

# path란?
app_name = 'account'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<username>/', views.profile, name='profile'), # 프로필 path
    path('<username>/follow', views.follow, name='follow'), # 추가기능) 팔로우 path
]
