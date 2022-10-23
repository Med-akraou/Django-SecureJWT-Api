from rest_framework.response import Response
from .models import Comptesespece,Imputationsespeces
from .serializers import ComptesespeceSerializer, ImputationsespecesSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status, filters
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.pagination import LimitOffsetPagination
import jwt
from django.core.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


# Create your views here.

class  ComptesespeceView(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        compte = Comptesespece.objects.all()
        serializer = ComptesespeceSerializer(compte, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ComptesespeceSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)



# get, put and delete by id
class  ComptesespeceView_pk(APIView):

    permission_classes = [IsAdminUser]
    def get_object(self,pk):
        try:
            return Comptesespece.objects.get(pk=pk)
        except Exception:
            raise Http404

            
    def get(self, request, pk):
        compte = self.get_object(pk)
        serializer = ComptesespeceSerializer(compte)
        return Response(serializer.data)
    

        
    def put(self, request, pk):
        compte = self.get_object(pk)
        serializer = ComptesespeceSerializer(compte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       


    def delete(self, request, pk):
            compte = self.get_object(pk)
            custmer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
       


#Imputationsespeces pagination
class ImputationsespecesPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

# Imputationsespeces
class ImputationsespecesList(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Imputationsespeces.objects.all()
    serializer_class = ImputationsespecesSerializer
    filter_backends = (DjangoFilterBackend)
    filter_fields = ('id',)
    pagination_class = ImputationsespecesPagination


class ImputationsespecesCreate(CreateAPIView):
    serializer_class = ImputationsespecesSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):        
           return super().create(request, *args, **kwargs)
        


class ImputationsespecesRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Imputationsespeces.objects.all()
    lookup_field = 'id'
    serializer_class = ImputationsespecesSerializer



