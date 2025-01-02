from functools import partial

from django.urls import path

from qlinks.views import health_check, short_link

urlpatterns = [
    path('', partial(short_link, path=''), name='short_link'),
    path('api/health_check', health_check, name='health_check'),
    path('<path:path>', short_link, name='short_link'),
]
