from django.urls import path
from .views import StudentListView, StudentCreateView, StudentDetailView

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('create/', StudentCreateView.as_view(), name='student_create'), 
    path('<int:student_id>/', StudentDetailView.as_view(), name='student_detail'),
]