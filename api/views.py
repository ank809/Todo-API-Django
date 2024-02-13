from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import TodoSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from  rest_framework.renderers import JSONRenderer

@csrf_exempt
def createTodo(request):
    if request.method=='POST':
        json_todo=request.body
        print("JSON Recieved", json_todo)
        stream=io.BytesIO(json_todo)
        print("Stream", stream)
        parsed_data=JSONParser().parse(stream)
        print("Parsed data",parsed_data)
        serializer= TodoSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('Data Saved', serializer.data)
        else:
            return HttpResponse(serializer.errors)
    return HttpResponse('METHOD NOT ALLOWED')
    
@csrf_exempt    
def read(request):
    if request.method=='GET':
        data=Todo.objects.all()
        serializer=TodoSerializer(data=data, many=True)
        serializer.is_valid()
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    return HttpResponse('Error')

@csrf_exempt
def update_todo(request, id):
    if request.method == 'PUT':
        json_data = request.body
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return HttpResponse('TODO NOT FOUND', status=404)

        stream = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream)
        serializer = TodoSerializer(todo, data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('TODO UPDATED')
        else:
            return HttpResponse(serializer.errors, status=400)
    else:
        return HttpResponse('Method Not Allowed', status=405)

@csrf_exempt
def delete_todo(request, id):
    if request.method=='DELETE':
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            return HttpResponse('TODO DELETED')
        except Todo.DoesNotExist:
            return HttpResponse('TODO NOT FOUND', status=404)
    else:
        return HttpResponse('METHOD NOT ALLOWED')