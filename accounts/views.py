from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import *

# Create your views here.

## 회원 가입 뷰
def signup(request):
    # 로그인한 사용자는 회원 가입 템플릿 액세스 제한
    if request.user.is_authenticated:
        # 피드 템플릿:view 연결
        return redirect('앱:view')
    # 회원 가입 폼이 제출 되었다면
    if request.method == 'POST': 
        # 회원 가입 폼 = 인스턴스 생성에 필요한 필드 데이터 제출 요청
        signupform = myUserCreationForm(request.POST)
        # 회원 가입 폼 유효성 검사 Form.is_valid()
        if signupform.is_valid():
            # 회원 가입 데이터 저장
            signupform.save()
            # 피드 템플릿:view 연결
            return redirect('앱:view')
    # 폼이 유효하지 않거나 요청 메서드가 POST가 아니면
    else:
        # 데이터가 없는 회원 가입 폼 인스턴스 생성
        signupform = myUserCreationForm()
    # 'form'이름으로 매핑된 유효하지 않은 데이터 필드 context를 렌더링
    context = {
        'form': signupform,
    }# 다시 회원 가입 템플릿 반환, context 출력
    return render(request, 'accounts/signup.html', context)

## 로그인 뷰
def signin(request):
    if request.method.is_authenticated:
        # 피드 템플릿:view 연결
        return redirect('앱:view')
    # 로그인 폼이 요청되면
    if request.method == 'POST':
        # 인증 요청, 유효성 검사를 위한 인스턴스 생성
        form = myAuthenticationForm(request, request.POST)
        
        if form.is_valid():
            # 양식이 유효한 경우 사용자는 제출된 폼 데이터와 연관된 사용자를 로그인시킵니다.
            login(request, form.get_user())
            # 피드 템플릿:view 연결
            return redirect('앱:view')
    # 폼이 유효하지 않거나 요청 메서드가 POST가 아니면
    else:
        # 데이터가 없는 로그인 폼 인스턴스 생성
        form = myAuthenticationForm()
    # 'form'이름으로 매핑된 유효하지 않은 데이터 필드 context를 렌더링
    context = {
        'form': form,
    }  # 다시 로그인 템플릿 반환, context 출력
    return render(request, 'accounts/login.html', context)

## 로그 아웃 뷰
# 로그인 인증된 유저만 엑세스
@login_required
def signout(request):
    # 로그인 인증된 요청 객체와 관련있는 인증된 유저의 세션을 로그아웃합니다.
    logout(request)
    return redirect('앱:view')

# 프로필 뷰
def profile(request, username):
    # 프로젝트에 활성화된 유저 모델을 검색하고 반환
    User = get_user_model()
    # 주어진 개체 username이 존재하지 않는다면 404 error 반환
    profile_owner = get_object_or_404(User, username=username)
    # 검색된 유저 인스턴스를 값으로 저장합니다.
    context = {
        'profile_owner': profile_owner
    }
    return render(request, 'accounts/profile.html', context)


## 추가 기능입니다 팔로우/팔로워 뷰
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
    return redirect('accounts:profile', username)
