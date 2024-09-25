from django.contrib import admin

from .models import (
    Faculty, Kafedra, Subject, Teacher, Group, Student
)
admin.site.register(Faculty)
admin.site.register(Group)
admin.site.register(Kafedra)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)

