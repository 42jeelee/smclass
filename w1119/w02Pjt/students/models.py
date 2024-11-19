from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=100)
  major = models.CharField(max_length=100)
  grade = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(4)])
  age = models.IntegerField(default=20, validators=[MinValueValidator(1)])
  gender = models.CharField(max_length=1, choices=[('M', '남'), ('F', '여')])
  hobbys = models.CharField(max_length=20)

  def __str__(self):
    return f"{self.name}[{self.age}]"
  
  class Meta:
    constraints = [
      models.CheckConstraint(
        check=models.Q(gender__in=['M', 'F']),
        name='check_gender'
      ),
    ]
