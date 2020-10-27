from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from .models import Node
from .serializers import nodeSerializer
from rest_framework.response import Response

@api_view(['GET'])
def homepage(request):
    node = Node.objects.all()
    serial = nodeSerializer(node , many=True )

    return Response(serial.data)