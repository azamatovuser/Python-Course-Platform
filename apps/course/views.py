from django.shortcuts import render, get_object_or_404
from apps.course.models import Course
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


@login_required
def list_course(request):
    all_courses = Course.objects.all()
    context = {
        "all_courses": all_courses
    }
    return render(request, 'list_course.html', context)


@login_required
def detail_course(request, pk):
    course = Course.objects.get(id=pk)
    context = {
        "course": course
    }
    return render(request, 'detail_course.html', context)