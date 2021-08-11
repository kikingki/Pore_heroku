from django.shortcuts import get_object_or_404, render
from user.models import Field
from django.db.models import Avg
from portfolio.models import Business, Portfolio

def fieldchoose(request):
    return render(request, 'average/fieldchoose.html')

def average(request, field_id):
    field = get_object_or_404(Field, pk=field_id)
    average = Business.objects.filter(status = "paid", field_id=field_id).values('price').aggregate(avg=Avg('price'))
    portfolio = Portfolio.objects.filter(f_id=field_id).order_by('-pf_date')[:2] # 포트폴리오 썸네일 띄우기
    return render(request, 'average/average.html', {'field':field, 'average':average, 'portfolio':portfolio})