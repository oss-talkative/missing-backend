from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import MChild
from .serializers import MChileSerializer

@api_view(['GET'])
def HelloAPI(request):
    return Response("Hello shinyeong!")

@api_view(['GET'])
def API(request):
    if request.method == 'GET':
        mchild = MChild.objects.all()
        serializer=MChileSerializer(mchild, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer=MChileSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
