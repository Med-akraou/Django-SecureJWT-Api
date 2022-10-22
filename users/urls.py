from django.urls import path
from .views import RegisterView , LoginView , UserViewJwt, LogoutView, UserView, UserRetrieveUpdateDestroy

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserViewJwt.as_view()),
    path('logout/', LogoutView.as_view()),
    path('users/',UserView.as_view()),
    path('users/<int:id>', UserRetrieveUpdateDestroy.as_view())
]