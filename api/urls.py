from django.urls import path
from.import views

urlpatterns = [
    #path('', views.apiOverview, name = 'apiOverview'),
    path('users-GET/', views.ShowAll, name ='users-GET'),
    path('users-detail/<int:pk>/', views.viewusers, name ='users-GET'),
    path('users-create/', views.createusers, name ='users-Create'),
    path('users-update/<int:pk>/', views.updateusers, name ='users-update'),
    path('users-delete/<int:pk>/', views.deleteusers, name ='users-delete'),
]
