from django.urls import path
from.import views

urlpatterns = [
    #path('', views.apiOverview, name = 'apiOverview'),
    path('citizens-GET/', views.ShowAll, name ='citizens-GET'),
    path('citizens-detail/<int:pk>/', views.Viewcitizens, name ='citizens-GET'),
    path('citizens-create/', views.Createcitizens, name ='citizens-Create'),
    path('citizens-update/<int:pk>/', views.Updatecitizens, name ='citizens-update'),
    path('citizens-delete/<int:pk>/', views.deletecitizens, name ='citizens-delete'),
]
