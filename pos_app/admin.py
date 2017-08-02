from django.contrib import admin
from pos_app.models import Items, Receipt

models = [
    Items,
    Receipt
]

admin.site.register(models)


