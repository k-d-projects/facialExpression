from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=122)
    desc=models.TextField()
    
    def __str__(self):
        return self.name

class Imgsave1(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=122)
    file1=models.FileField()
    value=models.TextField(blank=True)

    class Meta:
        db_table="img"

    def __str__(self):
        return self.name