from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/', obtain_auth_token, name='auth'),
    path('categories/', views.CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy'),
    path('expenses/', views.ExpenditureListCreateAPIView.as_view(), name='expenditure-list-create'),
    path('expenses/<int:pk>/', views.ExpenditureRetrieveUpdateDestroyAPIView.as_view(), name='expenditure-retrieve-update-destroy'),
    path('income/', views.IncomeListCreateAPIView.as_view(), name='income-list-create'),
    path('income/<int:pk>/', views.IncomeRetrieveUpdateDestroyAPIView.as_view(), name='income-retrieve-update-destroy'),
]