from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from .forms import signup_form
from django.contrib.auth import login, logout, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from feed.models import Post

def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(
                username=username,
                password=password
            )
            if user is not None:
                auth.login(request, user)
                return redirect('/feed')
        return redirect('/account/login')
    else:
        form = AuthenticationForm()
        return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    auth.logout(request)
    return redirect('/')


def signup_view(request):
    if request.method == "POST":
        form = signup_form(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('/feed')
        return render(request, 'account/signup.html', {'form': form})
    else:
        form = signup_form()
        return render(request, 'account/signup.html', {'form': form})
# 오류메세지 띄우기해야함

def profile(request, username):
    # 프로젝트에 활성화된 유저 모델을 검색하고 반환
    User = get_user_model()
    # 주어진 개체 username이 존재하지 않는다면 404 error 반환
    profile_owner = get_object_or_404(User, username=username)
    # 검색된 유저 인스턴스를 값으로 저장합니다.
    all_feed = Post.objects.all().order_by('-created_at')
    context = {
        'profile_owner': profile_owner,
        'feed' : all_feed
    }
    
    return render(request, 'account/profile.html', context)

def follow(request, username):
    User = get_user_model()
    writer = get_object_or_404(User, username=username)
    # 현재 로그인 중인 요청 객체로부터 관련된 유저를 검색합니다
    user = request.user
    # 작성자가 현재 로그인 요청 유저와 다른지 확인
    if writer != user:
        # 현재 로그인 중인 유저 pk가 팔로워 목록에 있는지 
        # 유저 모델 필드를 검색하고 User 모델 필드를 쿼리해서 
        # 작성자를 팔로우하고 있는지 확인
        if writer.followers.filter(pk=user.pk).exists():
            # 현재 로그인 중인 유저가 writer 팔로우 중이면 writer 팔로워 목록에서 유저 제거
            writer.followers.remove(user)
        else:
            # 팔로우 하고있지 않으면 팔로워 추가
            writer.followers.add(user)
    # 업데이트된 팔로워 목록이 반영된 유저 프로필 페이지로 리디렉션
    return redirect('account:profile', username)