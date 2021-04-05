from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from main_app.models import Blog
from main_app.models import Teams 

from .serializers import BlogSerializer
from .serializers import TeamsSerializer

class BlogAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogApiIndexView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class TeamsAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer

class BlogAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogAPINewView(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Blog.objects.all().order_by('-id')[:1] #Letest main_app
    serializer_class = BlogSerializer

    # Teams

class TeamsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer

class TeamsAPINewView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Teams.objects.all().order_by('-id')[:1] #Letest main_app
    serializer_class = TeamsSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)