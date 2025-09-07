from django.db import models

CATEGORY_CHOICES = [
    ('jersey', 'Jersey'),
    ('sepatu', 'Sepatu Bola'),
    ('aksesoris', 'Aksesoris'),
    ('lainnya', 'Lainnya'),
]

class Product(models.Model):
    nama = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='lainnya')
    thumbnail = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nama

