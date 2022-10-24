from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import User
from rest_framework import status
import jwt, datetime
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


#Customize claims of jwt to include some useful info on it especially role 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['name'] = user.first_name + " " + user.last_name
        token["role"] = user.role
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



# Create your views here.

# registration allowed to anyone
class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)

# get current user witout retreivig it from database, just from jwt
def get_current_user(request):
    token = request.META['HTTP_AUTHORIZATION']
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        token = token.replace('Bearer ',"")
        claims = jwt.decode(token, key='SECRET_KEY', algorithms=['HS256', ])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    return {"id":claims['user_id'], "name": claims["name"], "role":claims["role"]}

# CRUD User get all users

class UserView(APIView):

    permission_classes = [IsAuthenticated]
    def get(self, request):
        # checkif the current user is admin
        if get_current_user(request)["role"] != "admin":
            return Response({"Error": "Permission denied"}, status=401)
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

# get, update, delete by id
class  UserView_pk(APIView):

    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except Exception:
            raise Http404

            
    def get(self, request, id):
        # checkif the current user is admin
        if get_current_user(request)["role"] != "admin":
            return Response({"Error": "Permission denied"}, status=401)
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

    def put(self, request, id):
        # checkif the current user is admin
        if get_current_user(request)["role"] != "admin":
            return Response({"Error": "Permission denied"}, status=401)
        user = self.get_object(id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       


    def delete(self, request, id):
        # checkif the current user is admin
        if get_current_user(request)["role"] != "admin":
            return Response({"Error": "Permission denied"}, status=401)
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Get suspicious clients
class SuspiciousList(APIView):
    queryset = User.objects
    def get(self, request):
        # checkif the current user is admin
        if get_current_user(request)["role"] != "admin":
            return Response({"Error": "Permission denied"}, status=401)
        print(request.query_params)
        users = User.objects.raw("SELECT client.idpersonne FROM CLIENTS client"
        "INNER JOIN COMPTESESPECE compte ON client.IDPERSONNE = compte.IDCLIENT"
        "INNER JOIN IMPUTATIONSESPECES imputation ON compte.IDCOMPTE = imputation.IDCOMPTEESPECE"
        "WHERE imputation.DateEtat BETWEEN 2005-09-01 AND date('%s', '+3 year')"
        "AND imputation.Nature = 'F'"
        "GROUP BY client.IDPERSONNE"
        "HAVING SUM(CASE WHEN imputation.sens = 0 THEN imputation.montant END) >= (SUM(imputation.montant) * %s) / 36;",
        [request.query_params.get('year'),request.query_params.get('x')])
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

       



    





    