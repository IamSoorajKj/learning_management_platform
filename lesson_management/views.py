from django.shortcuts import render,get_object_or_404

from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import authentication,permissions

from module_management.models import Module

from lesson_management.serializers import LessonSerializer
from lesson_management.models import Lesson

# Create your views here.

class LessonCreateView(CreateAPIView):

  authentication_classes=[authentication.TokenAuthentication]

  permission_classes=[permissions.IsAuthenticated]

  serializer_class=LessonSerializer

  def perform_create(self,serializer):

    module_id=self.kwargs.get("pk")
    
    module_obj=get_object_or_404(Module,id=module_id)

    auth_user=self.request.user

    serializer.save(module=module_obj,created_by=auth_user)

class LessonRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

  authentication_classes=[authentication.TokenAuthentication]

  permission_classes=[permissions.IsAuthenticated]

  queryset=Lesson.objects.all()

  serializer_class=LessonSerializer
