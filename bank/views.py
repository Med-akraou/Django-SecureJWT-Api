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

# Create your views here.

class  ComptesespeceView(APIView):

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

   
    def get_object(self,pk):
        try:
            return Comptesespece.objects.get(pk=pk)
        except Exception:
            raise Http404
    
    def isAdmin(self,request):
        token = request.META['HTTP_AUTHORIZATION']
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return payload['role'] == 'Admin'

    def get(self, request, pk):
        if self.isAdmin(request):
            compte = self.get_object(pk)
            serializer = ComptesespeceSerializer(compte)
            return Response(serializer.data)
        raise PermissionDenied

        
    def put(self, request, pk):
        if self.isAdmin(request):
            compte = self.get_object(pk)
            serializer = ComptesespeceSerializer(compte, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        raise PermissionDenied


    def delete(self, request, pk):
        if self.isAdmin(request):
            compte = self.get_object(pk)
            custmer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise PermissionDenied


#Imputationsespeces pagination
class ImputationsespecesPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

# Imputationsespeces
class ImputationsespecesList(ListAPIView):
    queryset = Imputationsespeces.objects.all()
    serializer_class = ImputationsespecesSerializer
    filter_backends = (DjangoFilterBackend)
    filter_fields = ('id',)
    pagination_class = ImputationsespecesPagination

    def get_queryset(self):
        token = self.request.META['HTTP_AUTHORIZATION']
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        if payload['role'] == "Admin":
            return super().get_queryset()
        raise PermissionDenied

class ImputationsespecesCreate(CreateAPIView):
    serializer_class = ImputationsespecesSerializer

    def create(self, request, *args, **kwargs):
        token = self.request.META['HTTP_AUTHORIZATION']
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        if payload['role'] == "Admin":
           return super().create(request, *args, **kwargs)
        raise PermissionDenied


class ImputationsespecesRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Imputationsespeces.objects.all()
    lookup_field = 'id'
    serializer_class = ImputationsespecesSerializer



