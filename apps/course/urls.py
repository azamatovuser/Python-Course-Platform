from django.urls import path
from apps.course.views import index, list_course, detail_course


urlpatterns = [
    path('', index, name='index'),
    path('list/', list_course, name='list_course'),
    path('list/detail/<int:pk>/', detail_course, name='detail_course'),
]