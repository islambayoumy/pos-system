from django.contrib import admin
from pos_app.models import Items, Receipt, Receipts_Items

models = [
    Items,
    Receipt,
    Receipts_Items
]

admin.site.register(models)


