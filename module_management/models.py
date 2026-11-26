from django.db import models

# Create your models here.

from django.db import models
from django.utils.text import slugify #unique text creation in url

from course_management.models import Course

class Module(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="modules"
    )

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    description = models.TextField(blank=True)

    order = models.PositiveIntegerField(
        help_text="Module sequence within the course",
        null= True
    )



    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        module_instance = Module.objects.filter(course=self.course).last()

        #self=obj
        if not self.id: #only need to increment order in module creation  not module update.in module creation dont need id .but in update nedd id .thats why using if not self.id condition

            if module_instance:

                self.order = module_instance.order + 1
            else:
                self.order = 1

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    class Meta:
        ordering = ["order"]
        unique_together = ["course", "order"] #for correct order number 1->2->4 in this case 3 after two that why we use unique_together for correct order counting