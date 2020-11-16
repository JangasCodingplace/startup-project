from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Key


class KeyAdmin(admin.ModelAdmin):
    model = Key
    list_display = ('key', 'link_to_user', 'function', )
    search_fields = ('key', 'user__email', 'user__url_arg', )
    list_filter = ('function', )

    def link_to_user(self, obj=None):
        link = reverse("admin:user_user_change",
                       args=[obj.user.pk])
        return format_html('<a href="{}">{}</a>', link, obj.user.url_arg)


admin.site.register(Key, KeyAdmin)
