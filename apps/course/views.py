from django.shortcuts import render, get_object_or_404
from apps.course.models import Course


def index(request):
    return render(request, 'index.html')


def list_course(request):
    all_courses = Course.objects.all()
    context = {
        "all_courses": all_courses
    }
    return render(request, 'list_course.html', context)


def detail_course(request, pk):
    course = Course.objects.get(id=pk)
    print(course)
    context = {
        "course": course
    }
    return render(request, 'detail_course.html', context)