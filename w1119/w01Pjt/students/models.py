from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=100)
  major = models.CharField(max_length=100)
  grade = models.IntegerField(default=1)
  age = models.IntegerField(default=20)
  gender = models.CharField(max_length=1, choices=[('M', '남'), ('F', '여')])
  hobby = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  class Meta:
    constraints = [
      models.CheckConstraint(
        check=models.Q(gender__in=['M', 'F']),
        name='check_gender'
      ),
    ]
