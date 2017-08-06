from django.conf.urls import url
from pos_app.views import ItemsAPIview, ReceiptAPIview
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^items/$', ItemsAPIview.ItemsList.as_view(), name='items'),
    url(r'^receipt/$', ReceiptAPIview.ReceiptList.as_view(), name='receipt'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

