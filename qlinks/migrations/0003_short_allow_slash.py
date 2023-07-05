from django.db import migrations

import qlinks.fields


class Migration(migrations.Migration):
    dependencies = [
        ('qlinks', '0002_link_next_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short',
            field=qlinks.fields.ShortURLField(blank=True,
                                              help_text='the part of URL after / that will redirect to the long URL, e.g. https://my.short.link/[slug]',
                                              max_length=64, unique=True, verbose_name='short link slug'),
        ),
    ]
