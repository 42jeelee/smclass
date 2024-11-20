from django.db import models
from datetime import datetime

# Create your models here.
class Member(models.Model):
  id = models.CharField(max_length=50, primary_key=True)
  pw = models.CharField(max_length=100, blank=False)
  name = models.CharField(max_length=100)
  nickName = models.CharField(max_length=100)
  cdate = models.DateTimeField(default=datetime.now())

  def __str__(self):
    return f"{self.id}({self.name})"