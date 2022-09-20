from django.db import models

class Education(models.Model):
    institute = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    score = models.FloatField()

    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.institute

class Experience(models.Model):
    employer = models.CharField(max_length=50)
    proof = models.ImageField(default="images/certificate.png")
    employed = models.BooleanField()

    start = models.DateField()
    end = models.DateField()

    job_title = models.CharField(max_length=50)
    desc = models.TextField()

    location = models.CharField(max_length=60)

    def __str__(self):
        return self.employer + " " + self.job_title


class Skill(models.Model):
    type_choices = (
        ("Language","Language"),
        ("Framework", "Framework"),
        ("Tools", "Tools"),
        ("DataBase", "Database"),
        ("Soft Skills", "Soft Skills")
    )

    type_of = models.CharField(max_length=20, choices=type_choices)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
