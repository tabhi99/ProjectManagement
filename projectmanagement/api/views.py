# Create your views here.
from django.shortcuts import render
from .serializers import ClientSerializer,ProjectSerializer
from rest_framework import generics, permissions
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
            serializer.save(updated_at=timezone.now())

class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        client = generics.get_object_or_404(Client, pk=self.kwargs['client_id'])
        serializer.save(client=client, created_by=self.request.user)

class UserProjectsView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.projects.all()

