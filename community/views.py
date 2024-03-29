from community.forms import CommunityForm
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import CommunityForm, CmCommentForm
from .models import Category, Community
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from typing import ContextManager
from django.contrib import messages
from django.db.models import Q
import json

def community(request, com_id):
    categorys = get_object_or_404(Category, pk=com_id)
    # filter(), order_by() 사용
    communitys = Community.objects.filter(com_id=categorys).order_by('-post_date')
    q = request.GET.get('q', '')
    if q:
        communitys = communitys.filter(Q(post_title__icontains = q) | Q(post_content__icontains = q))
    # 5~10개 사이로 페이지를 나누는 게 좋을 것 같음.
    paginator = Paginator(communitys, 10)
    page = request.GET.get('page')
    # posts라는 객체를 따로 만들지 않고 communitys에 다시 대입해주면 됨.
    communitys = paginator.get_page(page)
    return render(request, 'community/community.html', {'communitys':communitys, 'categorys':categorys, 'q': q})

def cmwrite(request):
    if not request.user.is_active:
        return render(request, 'user/signin.html')
    
    if request.method == 'POST':
        form = CommunityForm(request.POST, request.FILES)
        if form.is_valid():
            community = form.save(commit=False)
            community.post_date = timezone.now()
            community.user_id = request.user
            community.save()
            return redirect('community', community.com_id.id)
    else:
        form = CommunityForm()
        return render(request, 'community/cmwrite.html', {'form':form})

def cmedit(request, id):
    community = get_object_or_404(Community, id=id)
    if request.method == 'POST':
        form = CommunityForm(request.POST, instance=community)
        if form.is_valid():
            community = form.save(commit=False)
            community.post_date = timezone.now()
            community.save()
            return redirect('cmdetail', id)
    else:
        form = CommunityForm(instance=community)
        return render(request, 'community/cmedit.html', {'form':form})

def cmdetail(request, id):
    community = get_object_or_404(Community, id=id)
    if request.method == 'POST':
        form = CmCommentForm(request.POST)
        if form.is_valid():
            cmcomment = form.save(commit=False)
            cmcomment.cm_id = community
            cmcomment.user_id = request.user
            cmcomment.cm_date = timezone.now()
            cmcomment.cm_comment = form.cleaned_data['cm_comment']
            cmcomment.save()
            return redirect('cmdetail', id)
    else:
        form = CmCommentForm()
        return render(request, 'community/cmdetail.html', {'community':community, 'form':form})

def cmdelete(request, id):
    community = get_object_or_404(Community, id=id)
    com_id = community.com_id.id
    community.delete()
    return redirect('community', com_id)

@login_required
@require_POST
def community_like(request):
    pk = request.POST.get('pk', None)
    community = get_object_or_404(Community, pk=pk)
    user = request.user

    if community.likes_user.filter(id=user.id).exists():
        community.likes_user.remove(user)
    
    else:
        community.likes_user.add(user)

    context = {'likes_count':community.count_likes_user()}
    return HttpResponse(json.dumps(context), content_type="application/json")