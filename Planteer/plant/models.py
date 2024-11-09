from django.db import models

class Plant(models.Model):
    CATEGORY_CHOICES = [
        ('herb', 'Herb'),
        ('tree', 'Tree'),
        ('flower', 'Flower'),
        ('vegetable', 'Vegetable'),
        ('fruit', 'Fruit'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_edible = models.BooleanField(default=False)
    description = models.TextField()
    image = models.ImageField(upload_to='plants/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

