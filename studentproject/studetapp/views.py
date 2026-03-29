from django.shortcuts import render,redirect
from.models import Student
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index_page(request):
    return render(request,"index.html")


@login_required(login_url='login')
def add_student(request):
    if request.method == 'POST':
      
      sname = request.POST.get('sname')
      sage = request.POST.get('age')
      sroll = request.POST.get('rollnumber')
      saddr = request.POST.get('address')
      if sname and sage and sroll and saddr :
         
        stud = Student(student_name = sname , student_age =sage , student_roll = sroll,student_addre = saddr)
        stud.save()
        messages.success(request,"Your informations is succssfuly saved.")
        return redirect('studentlist')

      else:
       messages.error(request,"please submit all form.")
       return redirect('addstudent')
        

    return render(request,'addstudent.html')
@login_required(login_url='login')

def student_list(request):
   stud = Student.objects.all()
   return render(request,'studentlist.html',{"student":stud})



@login_required(login_url='login')
def edit_student(request,id):
   stud = Student.objects.get(id=id)
   return render(request,'editstudent.html',{"data": stud})

@login_required(login_url='login')
def updat_stududet(request,id):
   stud = Student.objects.get(id = id )
   if request.method == "POST":
      stud.student_name = request.POST.get('sname')
      stud.student_age = request.POST.get('age')
      stud.student_roll = request.POST.get('rollnumber')
      stud.student_addre = request.POST.get('address')
      stud.save()
      return redirect("studentlist")
   
def delect_student(request,pk):
   stud = Student.objects.get(id = pk)
   stud.delete()
   return redirect('studentlist')

def register(request):
   if request.method == 'POST':
      data = request.POST
      un = data['uname']
      ue = data['uemail']
      up = data['upassword']
      cp = data['cpassword']
      if up == cp :
        User.objects.create_user(username = un ,email = ue , password = up)
        return redirect('login')
      
      elif User.objects.filter(username = un).exists():
         messages.error(request,"username is alreday used ")

      else:
           messages.error(request,"password does'not match")
           return redirect('register')
 


   return render(request,'register.html')

def log_in(request):
   if request.method == 'POST':
      data = request.POST
      un = data['uname']
      ue = data['uemail']
      up = data['upassword']
      User = authenticate(username = un , email = ue, password = up)
      if User is not None:
         login(request,User)
         messages.success(request, "Login successful", extra_tags='login')

         return redirect('indexpage')
      
      else:
         messages.error(request,'incorect email or password')
         return redirect("login")
         
   return render(request,"login.html")

def log_out(request):
   logout(request)
   messages.success(request, "Logout successful", extra_tags='logout')

   return redirect('indexpage')