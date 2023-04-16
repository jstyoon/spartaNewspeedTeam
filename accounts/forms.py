from django import forms
from .models import User
# 유저 등록 및 암호 생성을 위한 필드 및 유효성 검사를 제공 폼 클래스
from django.contrib.auth.forms import UserCreationForm
# 유저 인증을 위한 필드 및 유효성 검사 제공 폼 클래스
from django.contrib.auth.forms import AuthenticationForm


# 유저 생성 폼. UserCreationForm 상속.
class myUserCreationForm(UserCreationForm):
    # 폼 클래스 생성자 정의
    def __init__(self, *args, **kwargs):
        # 폼 초기화 및 슈퍼 클래스 생성자 호출
        super().__init__(*args,**kwargs)
        # 추가된 속성으로 업데이트할 필드 이름 목록
        class_update_fields = ['username', 'password1', 'password2']
        # class_update_fields 리스트 돌면서
        for field_name in class_update_fields:
            # css class form-control로 각 폼 필드의 widget.attrs dict 업데이트.
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })
    # 폼에서 메타 데이터 구성을 위해 중첩되는 클래스 정의
    class Meta:
        # 폼에 사용할 모델 지정
        model = User
        # 폼에 포함할 필드 지정. 유효성 검사에 필드 사용
        fields = ['username', 'password1', 'password2']

# 유저 인증 폼. AuthenticationForm 상속.
class myAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']