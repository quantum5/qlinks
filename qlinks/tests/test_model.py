from django.test import TestCase
from django.utils import timezone

from qlinks.models import Link


class LinkTestCase(TestCase):
    def setUp(self) -> None:
        Link.objects.create(
            short='short',
            long='https://long.example.com',
            is_working=True,
            last_check=timezone.now(),
        )

    def test_short_url(self):
        with self.settings(QLINKS_CANONICAL='https://short.example/'):
            self.assertEqual(
                Link.objects.get(short='short').short_url,
                'https://short.example/short'
            )
