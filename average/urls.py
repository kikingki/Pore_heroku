from django.urls import path
from average import views

urlpatterns = [
    path('fieldchoose/', views.fieldchoose, name='fieldchoose'),
    path('average/<int:field_id>', views.average, name='average'),
]