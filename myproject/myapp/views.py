from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import MChild
from .serializers import MChileSerializer

@api_view(['GET'])
def HelloAPI(request):
    return Response("Hello shinyeong!")

@api_view(['Post'])
def PostAPI(request):
        serializer=MChileSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Get'])
def GetAllAPI(request):
        mchild = MChild.objects.all()
        serializer=MChileSerializer(mchild, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def GetNameAPI(request):
    if request.method == 'POST':
        print("request:",request)
    mchild = MChild.objects.filter().all()
    serializer=MChileSerializer(mchild, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# @csrf_exempt
# def snippet_list(request):
#     if request.method == 'GET':
#         MChild = MChild.object.all()
#         serializer = MChileSerializer(MChild, many=True)
#         return JsonResponse(serializer.data, safe=False)