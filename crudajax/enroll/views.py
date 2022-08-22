from django.http import JsonResponse
from django.shortcuts import render
from django.urls import is_valid_path
from .models import User
from .forms import StudentForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def home(request):
    form=StudentForm()
    stud=User.objects.all()
    return render(request,'enroll/home.html',{'form':form,'stu':stud})

@csrf_exempt
def save_data(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            sid=request.POST['stuid']
            print("sid>>>>>",sid)
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            
            if(sid==''):
                user=User(name=name,email=email,password=password)
            else:
                user=User(id=sid,name=name,email=email,password=password)
            user.save()
            stud=User.objects.values()
            student_data=list(stud)
            print("---------------",student_data)
            return JsonResponse({'status':'save','student_data':student_data})
        else:
            return JsonResponse({'status':0})


@csrf_exempt
def delete_data(request):
    if request.method=="POST":
        id=request.POST.get('sid')
        print("________",id)
        pi=User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

@csrf_exempt
def edit_data(request):

    if request.method=="POST":
        id=request.POST.get('sid')
        print(">>>>>>>",id)
        student=User.objects.get(pk=id)
        student_data={"id":student.id,"name":student.name,"email":student.email,"password":student.password}
        return JsonResponse(student_data)






