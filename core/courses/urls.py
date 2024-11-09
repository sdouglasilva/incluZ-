from django.urls import path
from .views import CoursesListView, CoursesDetailView, CoursesCreateView

urlpatterns = [
    path('', CoursesListView.as_view(), name='course_list'),
    path('create/', CoursesCreateView.as_view(), name='course_create'), 
    path('<int:course_id>/', CoursesDetailView.as_view(), name='course_detail'),
]