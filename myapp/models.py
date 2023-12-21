from django.db import models

# Create your models here.
class BlogModel(models.Model):
    
    title = models.CharField(max_length=50)
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)

     