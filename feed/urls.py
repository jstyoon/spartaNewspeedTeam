from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # 04.11. 서경 url 연결
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # 홈 화면
    path('feed/', views.feed, name='feed'),  # 홈 화면 - 사용자가 로그인 하면 ~님 반갑습니다.에 id값 띄우기와 글쓰기 로그아웃 버튼으로 변경.


    # path('my_feed', views.user_feed, name='user_feed'),  # 마이페이지 및 프로필 수정

    # 기호님 게시글 수정
    # path('feed/modify/', views.modify_feed, name='modifiy'),
    path('feed/detail/<int:id>', views.view_feed, name='detail'),  # 상세보기
    path('feed/detail/modify/<int:id>', views.modify_feed, name='modify'),  # 수정
    #### upload_feed에서 modify_feed로변경
    path('feed/upload/', views.upload_feed, name='upload'), #업로드 피드
    path('feed/detail/delete/<int:id>', views.delete_feed, name='delete'),  # 삭제



]
