from functools import partial

from django.urls import path

from qlinks.views import short_link

urlpatterns = [
    path('', partial(short_link, path=''), name='short_link'),
    path('<path:path>', short_link, name='short_link'),
]
