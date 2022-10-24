from django.urls import path
from .views import ComptesespeceView, ComptesespeceView_id, ImputationsespecesCreate, ImputationsespecesList, ImputationsespecesView_id

urlpatterns = [
    # get all compte/ create compte
    path('comptes/', ComptesespeceView.as_view()),
    # get update delete compte
    path('compte/<int:id>', ComptesespeceView_id.as_view()),
    # create transaction
    path('createtransaction/', ImputationsespecesCreate.as_view()),
    # get all transaction 
    path('transactions/', ImputationsespecesList.as_view()),
    # get update delete tranaction by id 
    path('transaction/<int:id>', ImputationsespecesView_id.as_view())
]