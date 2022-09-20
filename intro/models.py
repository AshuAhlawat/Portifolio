from django.db import models

# Create your models here.

class Personal(models.Model):
    name = models.CharField(default="Ashwani Ahlawat", max_length=20)
    position = models.CharField(default="Instructor", max_length=25)
    dp = models.ImageField(default="images/dp.jpeg", upload_to="images")
    
    zipcode = models.IntegerField(default=100000)
    address = models.TextField(default="India, Haryana")
    
    phone = models.CharField(max_length=15,default="+91-9876543210")
    email = models.EmailField(default="ashwaniahlawat22@gmail.com")

    github = models.URLField(default="https://github.com/AshuAhlawat")
    linkdin = models.URLField(default="https://www.linkedin.com/in/ashwani-ahlawat/")
    other = models.URLField(default="https://myanimelist.net/animelist/Capti")

    about = models.TextField(default="Hey i am enjoing coding, print('Hello Darkness, my old friend')")


    def __str__(self):
        return self.name

