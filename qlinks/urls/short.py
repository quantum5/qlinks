from functools import partial

from django.urls import path

from qlinks.views import short_link

urlpatterns = [
    path('', partial(short_link, slug=''), name='short_link'),
    path('<slug>', short_link, name='short_link'),
]
