from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'), # 회원 가입 path
    path('login/', views.signin, name='signin'), # 로그인 path
    path('logout/', views.signout, name='signout'), # 로그아웃 path
    path('<username>/', views.profile, name='profile'), # 프로필 path
    path('<username>/follow', views.follow, name='follow'), # 추가기능) 팔로우 path
    
]