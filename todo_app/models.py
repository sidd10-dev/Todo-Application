from django.db import models

# Create your models here.
class Task(models.Model):
    work = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default = False)
    def __str__(self):
        return self.work
    