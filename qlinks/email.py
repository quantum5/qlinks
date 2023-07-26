from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.utils.translation import gettext as _

from qlinks.models import Link

template = get_template('qlinks/broken_email.txt')


def send_broken_email(link: Link):
    if link.created_by and link.created_by.email:
        emails = [link.created_by.email]
        name = link.created_by.get_full_name()
    else:
        emails = [email for name, email in settings.ADMINS]
        if not emails:
            return
        name = _('Admin')

    send_mail(
        subject=_('Broken link: %s') % link.short_url,
        message=template.render({
            'name': name,
            'link': link,
        }),
        from_email=None,
        recipient_list=emails,
    )
