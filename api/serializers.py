from rest_framework import serializers

from main_app.models import Blog
from main_app.models import Teams 

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog 
        # ('__all__')  for all fields
        # ['quote', 'author']
        fields = ['id', 'name', 'description', 'blog_img']

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams 
        # ('__all__')  for all fields
        # ['title']
        fields = ('__all__')
