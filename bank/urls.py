from django.urls import path
from .views import ComptesespeceView, ComptesespeceView_pk, ImputationsespecesCreate, ImputationsespecesList, ImputationsespecesRetrieveUpdateDestroy

urlpatterns = [
    path('comptes/', ComptesespeceView.as_view()),
    path('compte/<int:id>', ComptesespeceView_pk.as_view()),
    path('createtransaction/', ImputationsespecesCreate.as_view()),
    path('transactions/', ImputationsespecesList.as_view()),
    path('transaction/<int:id>', ImputationsespecesRetrieveUpdateDestroy.as_view())
]