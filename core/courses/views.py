import json
from .models import Courses
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import  method_decorator



@method_decorator(csrf_exempt, name='dispatch')
class CoursesListView(View):
    def get(self,request):
        courses = list(Courses.objects.values())
        return JsonResponse(courses, safe=False)
    


    
@method_decorator(csrf_exempt, name='dispatch')
class CoursesCreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        if not name or not description:
            return JsonResponse({'Erro':'Nome e descrição são necessários.'})
        course = Courses.objects.create(
            name=name,
            description=description
        )
        return JsonResponse({'id': course.id}, status = 201)


    
@method_decorator(csrf_exempt, name='dispatch')
class CoursesDetailView(View):
    
    def get(self, request, course_id):
        course = get_object_or_404(Courses, id = course_id)
        data = {
            'id': course.id,
            'name': course.name,
            'description': course.description,
        }
        return JsonResponse(data)
    
    def put(self, request, course_id):
        course = get_object_or_404(Courses, id=course_id)
        data = json.loads(request.body)
        course.name = data.get('name', course.name)
        course.description = data.get('description', course.description)
        course.save()
        
        return JsonResponse({
            'id': course.id,
            'name': course.name,
            'description': course.description
        })
    
    def delete(self, request, course_id):
        student = get_object_or_404(Courses, id=course_id)
        student.delete()
   
        return JsonResponse({}, status=204)