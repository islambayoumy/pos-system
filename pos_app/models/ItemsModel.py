from django.db import models

class Items(models.Model):
    
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    stock_amount = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Items'
        ordering = ['-timestamp']

    def __str__(self):
        return self.name

