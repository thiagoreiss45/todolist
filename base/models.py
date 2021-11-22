from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS_CHOICES = (
    ('Not started', 'Not started'),
    ('In progress', 'In progress'),
    ('Done', 'Done'),
)

class Task(models.Model):
    user = models.ForeignKey(
        User,on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    complete = models.CharField(max_length=100, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.title

    class Meta:
        ordering = ['complete']
    