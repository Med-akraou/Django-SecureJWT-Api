from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, UserView, UserView_pk, MyTokenObtainPairView, SuspiciousList

urlpatterns = [
    # login
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # sing up
    path('register/', RegisterView.as_view()),
    # get all users
    path('users/',UserView.as_view()),
    # get update delete user by id 
    path('users/<int:id>', UserView_pk.as_view()),
    # Suspicious list users
    path('suspicioususers/', SuspiciousList.as_view()),
]