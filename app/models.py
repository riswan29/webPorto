from django.db import models
class CategoryBlogModels(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class BlogModels(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(CategoryBlogModels, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
