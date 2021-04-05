from django.urls import path

from .views import BlogAPIView
from .views import TeamsAPIView
from .views import BlogAPIDetailView
from .views import BlogAPINewView
from .views import TeamsAPIDetailView
from .views import TeamsAPINewView

from .views import BlogApiIndexView
from .views import HelloView



urlpatterns = [
    path('', BlogAPIView.as_view()),
    path('main_app/blog', BlogAPIView.as_view()),
    path('main_app/blog/<int:pk>/', BlogAPIDetailView.as_view()),
    path('main_app/blog/new/', BlogAPINewView.as_view()),
    path('blog/', BlogApiIndexView.as_view()),


    path('main_app/teams', TeamsAPIView.as_view()),
    path('main_app/teams/<int:pk>/', TeamsAPIDetailView.as_view()),
    path('main_app/teams/new/', TeamsAPINewView.as_view()),
    path('hello/', HelloView.as_view(), name='hello'),
]