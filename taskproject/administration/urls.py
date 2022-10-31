# from administration.models import Branch
from django.urls import path
from administration import views

app_name = 'administration'
urlpatterns = [
    path('', views.home, name='home'),
    path('sign-up/', views.add_user, name='add_user'),   
    path('edit-user/<str:pk>/', views.UserUpdate.as_view(), name='edit_user'),
    path('user-detail/<str:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('delete-user/<str:pk>/', views.delete_user, name='delete_user'),
]
