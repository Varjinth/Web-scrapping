from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Product(models.Model):
    url = models.URLField(max_length=200, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100,default='unknown')
    size = models.CharField(max_length=100,default='unknown')
    image = models.CharField(max_length=100,default='unknown')  
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='unknown')
    scraped_at = models.DateTimeField(auto_now_add=True,)
    
    def __str__(self):
        return self.title



