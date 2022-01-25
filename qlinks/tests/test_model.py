from django.test import TestCase, override_settings
from django.utils import timezone

from qlinks.models import Link


@override_settings(QLINKS_CANONICAL='https://short.example/')
class LinkTestCase(TestCase):
    def setUp(self) -> None:
        Link.objects.create(
            short='short',
            long='https://long.example.com',
            is_working=True,
            last_check=timezone.now(),
        )

    def test_short_url(self):
        self.assertEqual(
            Link.objects.get(short='short').short_url,
            'https://short.example/short'
        )
