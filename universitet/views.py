from django.shortcuts import render

from .models import (
    Faculty, Kafedra, Subject, Teacher, Group, Student
)


def home(request):
    return render(request, 'home.html')


def faculty_list(request):
    faculties = Faculty.objects.all()
    ctx = {'faculties': faculties}
    return render(request, 'faculty-list.html', ctx)


def kafedra_list(request):
    kafedras = Kafedra.objects.all()
    ctx = {'kafedras': kafedras}
    return render(request, 'kafedra-list.html', ctx)


def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'group-list.html', ctx)


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'student-list.html', ctx)


def subject_list(request):
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request, 'subject-list.html', ctx)


def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teacher-list.html', ctx)
