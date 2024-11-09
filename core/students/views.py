import json
from .models import Student
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import  method_decorator


@method_decorator(csrf_exempt, name='dispatch')

class StudentListView(View):
    def get(self,request):
        students = list(Student.objects.values())
        return JsonResponse(students, safe=True)


@method_decorator(csrf_exempt, name='dispatch')

class StudentCreateView(View):
    def post(self, request):
        data = json.loads(request.body)

        student = Student.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            date_of_birth = data['date_of_birth'],

        )
        if 'courses' in data:
            student.courses.set(data['courses'])
        
        return JsonResponse({'id': student.id}, status = 201)

@method_decorator(csrf_exempt, name='dispatch')

class StudentDetailView(View):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id = student_id)
        data = {
            'id': student.id,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'date_of_birth': student.date_of_birth,
            'email': student.email,
            'courses': list(student.courses.values_list('name', flat = True))
        }
        return JsonResponse(data)
    
    def put(self, request, student_id):
        # Obter o estudante ou retornar 404
        student = get_object_or_404(Student, id=student_id)

        # Carregar os dados enviados pela requisição
        data = json.loads(request.body)

        # Atualizar os campos do estudante conforme os dados recebidos
        student.first_name = data.get('first_name', student.first_name)
        student.last_name = data.get('last_name', student.last_name)
        student.email = data.get('email', student.email)
        student.date_of_birth = data.get('date_of_birth', student.date_of_birth)

        # Salvar o estudante com os dados atualizados
        student.save()
    

    def delete(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return JsonResponse({'message': 'Student deleted'}, status=204)



