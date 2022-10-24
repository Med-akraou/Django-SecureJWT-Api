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
from rest_framework.permissions import IsAuthenticated
from users.views import get_current_user


# Create your views here.

class  ComptesespeceView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        # check if whether the current user is admin
        if get_current_user(request)["role"] != "admin":
            return Response({"Error": "Permission denied"}, status=401)
        compte = Comptesespece.objects.all()
        serializer = ComptesespeceSerializer(compte, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        # check if the user can create a compte (compteCreator)
        if get_current_user(request)["role"] != "compteCreator":
            return Response({"Error": "Permission denied"}, status=401)
        serializer = ComptesespeceSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)



# get, put and delete by id
class  ComptesespeceView_id(APIView):

    permission_classes = [IsAuthenticated]
    def get_object(self,id):
        try:
            return Comptesespece.objects.get(pk=id)
        except Exception:
            raise Http404

            
    def get(self, request, id):
        if get_current_user(request)["role"] != "admin":
            return Response({"Error": "Permission denied"}, status=401)
        compte = self.get_object(id)
        serializer = ComptesespeceSerializer(compte)
        return Response(serializer.data)
    

        
    def put(self, request, id):
        if get_current_user(request)["role"] != "admin":
            return Response({"Error": "Permission denied"}, status=401)
        compte = self.get_object(id)
        serializer = ComptesespeceSerializer(compte, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       


    def delete(self, request, id):
        if get_current_user(request)["role"] != "admin":
            return Response({"Error": "Permission denied"}, status=401)
        compte = self.get_object(id)
        compte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       


#Imputationsespeces pagination
class ImputationsespecesPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

# Imputationsespeces
class ImputationsespecesList(ListAPIView):
    queryset = Imputationsespeces.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ImputationsespecesSerializer
    pagination_class = ImputationsespecesPagination
    def list(self,request):
        # check if whether the current user is admin
        if get_current_user(request)["role"] != "admin":
            return Response({"Error": "Permission denied"}, status=401)
        queryset = self.get_queryset()
        serializer = ImputationsespecesSerializer(queryset, many=True)
        return Response(serializer.data)


class ImputationsespecesCreate(CreateAPIView):
    serializer_class = ImputationsespecesSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):  
        return super().create(request, *args, **kwargs)
        


class   ImputationsespecesView_id(APIView):

    permission_classes = [IsAuthenticated]
    def get_object(self,id):
        try:
            return Imputationsespeces.objects.get(pk=id)
        except Exception:
            raise Http404

            
    def get(self, request, id):
        if get_current_user(request)["role"] != "admin":
            return Response({"Error": "Permission denied"}, status=401)
        transaction = self.get_object(id)
        serializer = ImputationsespecesSerializer(transaction)
        return Response(serializer.data)
    

        
    def put(self, request, id):
        if get_current_user(request)["role"] != "admin":
            return Response({"Error": "Permission denied"}, status=401)
        transaction = self.get_object(id)
        serializer = ImputationsespecesSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       


    def delete(self, request, id):
        if get_current_user(request)["role"] != "admin":
            return Response({"Error": "Permission denied"}, status=401)
        transaction = self.get_object(id)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



       



