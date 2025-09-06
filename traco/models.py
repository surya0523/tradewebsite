from django.db import models
 
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
 
    def __str__(self):
        return self.name
 
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    read_time = models.CharField(max_length=50)  # e.g. "5 Mins Read"
    date = models.DateField()
    image = models.ImageField(upload_to="blogs/", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
 
    def __str__(self):
        return self.title
    
class Partner(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    pincode = models.CharField(max_length=6)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name