from django.db import models

# Create your models here.
class Member(models.Model):
  id = models.CharField(max_length=100, primary_key=True)
  pw = models.CharField(max_length=100, blank=False)
  name = models.CharField(max_length=100)
  nicName = models.CharField(max_length=100, null=True)
  mdate = models.DateField(auto_now=True)

  def __str__(self):
    return f"{self.id}({self.name})"
