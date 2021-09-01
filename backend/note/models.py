from user.models import User
from django.db import models

# Create your models here.
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=False)