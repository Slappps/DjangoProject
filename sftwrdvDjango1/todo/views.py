from django.shortcuts import render
from django.shortcuts import HttpResponse, render

from .models import TodoItem
# Create your views here.


def home(request):
    return render(request, 'home.html')

def mydata(request):
    latest_data_list = TodoItem.objects.all()
    context = {"latest_data_list": latest_data_list}

    if request.method == 'POST':
        print(request.POST)
        if 'send' in request.POST:
            if request.POST['date'] !='' and request.POST['desc'] != '':
                print("add")
                try:
                    val1 = request.POST['date']
                    val2 = request.POST['desc']
                    newTodo = TodoItem(due_date=val1, todo_text=val2)
                    print(newTodo)
                    newTodo.save()
                except:
                    pass
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            print("items:: ", TodoItem.objects.values_list('id', flat=True))

            if int(pk) in TodoItem.objects.values_list('id', flat=True):

                item = TodoItem.objects.get(id = pk)
                item.delete()

        for x in TodoItem.objects.all():
            print(x.id)
            if str(x.id) in request.POST.getlist('check'):
                print("True")
                x.completed = True
                x.save()
            else:
                print("false")
                x.completed = False
                x.save()




    return render(request, "home.html", context)

def add(request):

    return HttpResponse("add function")