from django.db import models
from professional.models import Skill,Experience
# Create your models here.

class Project(models.Model):
    cover = models.ImageField(default="images/cover.jpg")
    name = models.CharField(max_length=100)
    desc = models.TextField(default="")
    link = models.URLField(default="https://github.com/AshuAhlawat")

    completed = models.DateField()
    skills = models.ManyToManyField(Skill)

    on_job = models.ForeignKey(Experience, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    cover = models.ImageField(default="images/certificate.png")
    org = models.CharField(max_length=30)
    
    name = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField()

    def __str__(self):
        return f"{self.name} - {self.org}"

        
class Achievement(models.Model):
    data = models.TextField()
