from django.db import models

# Create your models here.
class Board(models.Model):
  bno = models.AutoField(primary_key=True)
  id = models.CharField(max_length=100)
  # member = models.ForeignKey(Member, on_delete=models.DO_NOTHING, null=False)
  btitle = models.CharField(max_length=1000)
  bcontent = models.TextField()
  bgroup = models.IntegerField(null=True)
  bstep = models.IntegerField(default=0)
  bindent = models.IntegerField(default=0)
  bhit = models.IntegerField(default=0)
  bdate = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"{self.bno}({self.id}) {self.btitle}"