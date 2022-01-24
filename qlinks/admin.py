from django.conf import settings
from django.contrib import admin
from django.template.defaultfilters import truncatechars
from django.utils import timezone
from django.utils.html import format_html
from django.utils.translation import gettext, gettext_lazy as _

from qlinks.health import check_url
from qlinks.models import Link


class LinkAdmin(admin.ModelAdmin):
    fields = ('short', 'long', 'created_by', 'created_on', 'updated_on', 'is_working', 'last_check')
    readonly_fields = ('created_by', 'created_on', 'updated_on', 'is_working', 'last_check')
    list_display = ('short', 'long_url', 'created_by', 'created_on', 'updated_on', 'is_working', 'last_check', 'short_url')
    list_filter = ('created_by', 'is_working', 'created_on', 'updated_on')
    search_fields = ('short', 'long')

    @admin.display(ordering='long', description=_('long URL'))
    def long_url(self, obj):
        return format_html('<a href="{0}">{1}</a>', obj.long, truncatechars(obj.long, 64))

    @admin.display(description=_('link'))
    def short_url(self, obj):
        if settings.QLINKS_CANONICAL:
            return format_html('<a href="{0}{1}">{2}</a>', settings.QLINKS_CANONICAL, obj.short, gettext('Link'))

    def save_model(self, request, obj: Link, form, change):
        obj.created_by = request.user
        obj.updated_on = timezone.now()
        obj.is_working = check_url(obj.long)
        obj.last_check = timezone.now()
        super().save_model(request, obj, form, change)


admin.site.register(Link, LinkAdmin)
