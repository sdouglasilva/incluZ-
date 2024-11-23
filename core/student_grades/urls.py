from django.urls import path
from .views import GradeListView, GradeCreateView, GradeDetailView, GradeDeleteView

urlpatterns = [
    path('', GradeListView.as_view(), name='grade_list'),  
    path('create/', GradeCreateView.as_view(), name='grade_create'),
    path('<int:pk>/', GradeDetailView.as_view(), name='grade_detail'),  
    path('<int:pk>/delete/', GradeDeleteView.as_view(), name='grade_delete'),
    
]