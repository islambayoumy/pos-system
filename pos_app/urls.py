from django.conf.urls import url
from pos_app.views import ItemsAPIview
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^items/$', ItemsAPIview.ItemsList.as_view(), name='items'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

