from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

new_index = 3

tasks = {

    0: "bli buke",
    1: "laj rrobat",
    2: "praktiko kodim",
}

def home(request):
    return render(request, "index.html", {"tasks": tasks})

@csrf_exempt
def new(request): 
    global new_index
    tasks.update({new_index:request.POST.get('new_task')})  
    new_index += 1
    return render(request, "index.html", {"tasks": tasks})

def delete(request):
    tasks.pop(int(request.POST.get('delete_id')))
    return render(request, "index.html", {"tasks": tasks})