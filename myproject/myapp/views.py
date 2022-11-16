from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MChild
from .serializers import MChileSerializer

# Create your views here.

@api_view(['Post'])
def addFoundChild(request):
        serializer=MChileSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get'])
def allFoundChild(request):
        mchild = MChild.objects.all()
        serializer=MChileSerializer(mchild, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['Get', 'Post'])
def FoundChild(request):
    if(request.method == 'POST'):
        serializer=MChileSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        mchild = MChild.objects.all()
        serializer=MChileSerializer(mchild, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST', 'GET'])
def nameFoundChild(request):
    if request.method == 'POST':
        print("----------------", request.data)
        post=MChild.objects.filter(name=request.data['name']).all()
        serializer=MChileSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    mchild = MChild.objects.filter().all()
    serializer=MChileSerializer(mchild, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
