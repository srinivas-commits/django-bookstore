from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class library_manager(models.Model):
    topic_title = models.CharField(max_length=15, null=True)
    slug = models.SlugField(null=True)
    date = models.DateField(auto_now_add=True)
    overview = models.TextField(null=True) 
    img =  models.ImageField(default='default.png', blank=True , null=True)
    stored_file = models.FileField(default='default.pdf', blank=True , null=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.topic_title



