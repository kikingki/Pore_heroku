from django import forms
from django.db import models
from django.forms import fields
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


#model에 넣은대로 입력되게 했어요
class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'password', 'nickname', 'account', 'cr_id', 'field_id']
        # 회원가입에 필드 이름 대신 띄우는 문자열
        labels = {
            'username': '아이디',
            'name': '이름',
            'password': '비밀번호',
            'nickname': '닉네임',
            'account': '계좌번호',
            'cr_id': '경력',
            'field_id': '직업'
        }

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "비밀번호나 이메일이 올바르지 않습니다. 다시 확인해 주세요."
        ),
        'inactive': ("이 계정은 인증되지 않았습니다. 인증을 먼저 진행해 주세요."),
    }

    def __init__(self, request=None, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs) # 꼭 있어야 한다!
        self.fields['username'].label = '아이디'    # 수정
        self.fields['password'].label = '비밀번호'
    

