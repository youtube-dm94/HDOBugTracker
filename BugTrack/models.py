from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Ticket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE , related_name='user')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "text : " + self.text

    class Meta:
        ordering = ['-created']