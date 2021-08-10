from django import forms
from django.db.models.fields import CommaSeparatedIntegerField
from django.forms import fields
from .models import CmComment, Community
from django_summernote.widgets import SummernoteWidget

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['com_id', 'post_title', 'post_content']

        labels = {
            'com_id': '게시판 종류 선택',
            'post_title': '게시글 제목',
            'post_content': '게시글 내용',
        }

        widgets = {
            'post_content': SummernoteWidget(),
        }

class CmCommentForm(forms.ModelForm):
    class Meta:
        model = CmComment
        fields = ['cm_comment']
        
        labels = {
            'cm_comment': '댓글',
        }
