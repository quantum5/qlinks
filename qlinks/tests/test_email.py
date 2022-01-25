from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase, override_settings
from django.utils import timezone

from qlinks.email import send_broken_email
from qlinks.models import Link


@override_settings(
    QLINKS_CANONICAL='https://short.example/',
    QLINKS_BROKEN_EMAIL=True,
)
class EmailTest(TestCase):
    def create_link(self, user) -> Link:
        return Link.objects.create(
            short='short',
            long='https://long.example.com',
            created_by=user,
            is_working=False,
            last_check=timezone.now(),
        )

    def assert_email(self, link: Link, name: str, to: str):
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual([to], mail.outbox[0].to)
        self.assertIn(link.short_url, mail.outbox[0].subject)
        self.assertIn(link.short_url, mail.outbox[0].body)
        self.assertIn(link.long, mail.outbox[0].body)
        self.assertIn(f'Dear {name},', mail.outbox[0].body)

    def test_send_no_user(self):
        link = self.create_link(None)
        with self.settings(ADMINS=[('someone', 'someone@example.com')]):
            send_broken_email(link=link)
        self.assert_email(link, 'Admin', 'someone@example.com')

    def test_send_user(self):
        link = self.create_link(User.objects.create_user(
            'test', email='user@example.com', first_name='Test', last_name='User'
        ))
        send_broken_email(link=link)
        self.assert_email(link, 'Test User', 'user@example.com')

    def test_send_user_no_email(self):
        link = self.create_link(User.objects.create_user('test', first_name='Test', last_name='User'))
        with self.settings(ADMINS=[('someone', 'someone@example.com')]):
            send_broken_email(link=link)
        self.assert_email(link, 'Admin', 'someone@example.com')
