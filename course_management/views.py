from django.shortcuts import render,get_object_or_404

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from course_management.serializers import CourseSerializer
from course_management.models import Course

from accounts.permissions import IsOwner

# Create your views here.



class CourseListCreateView(ListCreateAPIView):

  serializer_class=CourseSerializer

  authentication_classes=[authentication.TokenAuthentication]

  permission_classes=[permissions.IsAuthenticated]

  #overriding this method to get all courses of this user
  def get_queryset(self):
    
    return Course.objects.filter(trainer=self.request.user)

  def perform_create(self, serializer):

    serializer.save(trainer=self.request.user)

class CourseRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

  authentication_classes=[authentication.TokenAuthentication]

  permission_classes=[IsOwner]

  serializer_class=CourseSerializer

  def get_queryset(self):

    return Course.objects.filter(trainer=self.request.user)




