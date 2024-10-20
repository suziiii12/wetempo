from django.shortcuts import render, redirect
from .models import Post, Schedule
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



# Create your views here.
def index(request):
    return render(request,'main/index.html')

def blog(request):
    schedules = Schedule.objects.all()  # Schedule 모델의 모든 객체를 가져오는 쿼리셋
    return render(request, 'main/blog.html', {'schedules': schedules})

def posting(request, pk):
    post = Schedule.objects.get(pk=pk)

    return render(request, 'main/posting.html', {'schedule':Schedule})

def new_post(request):
    if request.method == 'POST':
        new_article=Schedule.objects.create(
                friend_name=request.POST['friend_name'],
                summary=request.POST['summary'],
                dtstart=request.POST['dtstart'],
                dtend=request.POST['dtend'],
                location=request.POST['location'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')

def get_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # JS에서 보내온 JSON 데이터를 파싱
            print(data)  # 받은 데이터를 출력하거나 처리
            return JsonResponse({'status': 'success', 'received': data})  # 성공 응답
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)