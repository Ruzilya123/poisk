from django.http import HttpResponse
  
def index(request):
    return HttpResponse("<h2>Главная</h2>")
 
def user(request):
    age = request.GET.get("age")
    name = request.GET.get("name")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")