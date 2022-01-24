from django.urls import path

from qlinks.views import short_link

urlpatterns = [
    path('<slug>', short_link, name='short_link'),
]
