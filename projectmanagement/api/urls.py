# myapp/urls.py
from django.urls import path,include
from .views import ClientListCreateView, ClientDetailView, ProjectCreateView, UserProjectsView
from api import views

urlpatterns = [    
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/', UserProjectsView.as_view(), name='user-projects'),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    
]
