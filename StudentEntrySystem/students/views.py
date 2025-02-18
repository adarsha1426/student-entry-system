from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.http import JsonResponse
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def add_student(request):
    if request.method == "POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_student')
    else:
        form=StudentForm()
    return render(request,'students/add_student.html',{'form':form})

def update_student(request,student_id):
    student=get_object_or_404(Student,id=student_id)
    print(student_id)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_student')
    else:
        form=StudentForm(instance=student)
    return render(request,'students/update_student.html',{'form':form,'student':student})

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('view_student')        

def view_student(request):
    students=Student.objects.all()
    return render(request,'students/student_list.html',{'students':students})
#to retrieve and add student
@api_view(['GET','POST'])
def student_list(request):
    students=Student.objects.all()
    serializer=StudentSerializer(students,many=True)
    if request.method=="GET":
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Added students successfully",status=status.HTTP_201_CREATED)
        else:
            serializer=StudentSerializer()
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#to update and delete the student
@api_view(['PUT'])
def student_update_api_view(request,id):
    try:
        student=Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response("Student Not found",status=status.HTTP_400_BAD_REQUEST)
    if request.method=="PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['DELETE'])
def student_delete_api_view(request,id):
    try:
        student=Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response("Student Not found")
    student.delete()
    return Response({"message": "Deleted the student record"}, status=status.HTTP_204_NO_CONTENT)