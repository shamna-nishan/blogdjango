from django.shortcuts import render  
from myapp . form import StudentForm  
  

# Create your views here.
def index(request):  
    student = StudentForm()  
    return render(request,"index.html",{'form':student})  
