from django.db import models
from pos_app.models import Items

class Receipt(models.Model):
    
    paid_amount = models.FloatField(default=0.0)
    is_paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Receipts'

    def __str__(self):
        return "Receipt " + str(self.pk)


class Receipts_Items(models.Model):

    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    total_item_amount = models.FloatField(default=0.0)
    paid_amount_per_item = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Receipts_Items'

    def __str__(self):
        return str(self.pk)


