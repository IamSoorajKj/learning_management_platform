from rest_framework import serializers

from course_management.models import Course

from lesson_management.models import Lesson

from django.db.models import Sum

from module_management.models import Module
from module_management.serializers import ModuleSerializer


class CourseSerializer(serializers.ModelSerializer):

  course_duration=serializers.SerializerMethodField(read_only=True)


  module_count=serializers.SerializerMethodField(read_only=True)

  modules=serializers.SerializerMethodField(read_only=True)

  class Meta:
    model=Course
    fields="__all__"
    read_only_fields=['id','trainer','slug','created_at','updated_at']

  
  def get_module_count(self,obj):
    
    return Module.objects.filter(course=obj).count()
  
  def get_modules(self,obj):

    qs=Module.objects.filter(course=obj)

    serializer_instance=ModuleSerializer(qs,many=True)

    return serializer_instance.data

  def get_course_duration(self,obj):

    return Lesson.objects.filter(module__course=obj).values("duration").aggregate(total=Sum("duration")).get("total",0)
    #lesson model have only module no course so first take module then take the course match with obj 


  

