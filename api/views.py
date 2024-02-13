from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import TodoDeSerializer, TodoSerializer
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
        serializer= TodoDeSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('Data Saved', serializer.data)
    
        return HttpResponse('error')
    
@csrf_exempt    
def read(request):
    if request.method=='GET':
        data=Todo.objects.all()
        serializer=TodoSerializer(data=data, many=True)
        serializer.is_valid()
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    return HttpResponse('Error')

