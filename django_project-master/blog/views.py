
from django.http import JsonResponse
from .models import Student

def index(request):
    s = Student.objects.create(
        first_name="John", last_name="Travolta", email ="john@gmail.com"
    )
    print(s)
    return JsonResponse({'msg':"University app"})