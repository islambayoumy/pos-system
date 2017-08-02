from django.db import models
from pos_app.models import Items

class Receipt(models.Model):
    
    item = models.ManyToManyField(Items)
    total_amount = models.FloatField(default=0.0)
    paid_amount = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Receipts'
        ordering = ['-timestamp']

    def __str__(self):
        return self.pk

