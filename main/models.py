from django.db import models
import uuid
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('jersey', 'Jersey'),
    ('sepatu', 'Sepatu Bola'),
    ('aksesoris', 'Aksesoris'),
    ('lainnya', 'Lainnya'),
]

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='lainnya')
    thumbnail = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    product_views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()