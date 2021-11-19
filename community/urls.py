from typing import Pattern
from django.urls import path
from community import views

urlpatterns = [
    path('community/<int:com_id>', views.community, name='community'),
    path('cmwrite/', views.cmwrite, name='cmwrite'),
    path('cmedit/<int:id>/', views.cmedit, name='cmedit'),
    path('cmdetail/<int:id>/', views.cmdetail, name='cmdetail'),
    path('delete/<int:id>/', views.cmdelete, name='cmdelete'),
    path('like/', views.community_like, name='community_like'),
]