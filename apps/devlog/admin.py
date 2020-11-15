from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Version, Patch, Commit


class PatchInline(admin.StackedInline):
    model = Patch
    extra = 1


class VersionAdmin(admin.ModelAdmin):
    model = Version
    list_display = ('__str__', 'patchcount', )
    search_fields = ('version', )
    inlines = (PatchInline, )


admin.site.register(Version, VersionAdmin)


class CommitInline(admin.StackedInline):
    model = Commit


class PatchAdmin(admin.ModelAdmin):
    model = Patch
    list_display = ('__str__', 'link_to_version', )
    search_fields = ('key', 'version__version', )
    list_filter = ('version__version', )
    inlines = (CommitInline, )

    def link_to_version(self, obj=None):
        link = reverse("admin:devlog_version_change",
                       args=[obj.version.pk])
        return format_html('<a href="{}">{}</a>', link, obj.version)


admin.site.register(Patch, PatchAdmin)


class CommitAdmin(admin.ModelAdmin):
    model = Commit
    list_display = ('commit', 'link_to_version', 'link_to_patch')
    list_filter = ('version__version', )
    search_fields = ('version__version', 'patch__key', )

    def link_to_version(self, obj=None):
        link = reverse("admin:devlog_version_change",
                       args=[obj.version.pk])
        return format_html('<a href="{}">{}</a>', link, obj.version)

    def link_to_patch(self, obj=None):
        link = reverse("admin:devlog_version_change",
                       args=[obj.patch.pk])
        return format_html('<a href="{}">{}</a>', link, obj.patch)

    def commit(self, obj=None):
        commit = obj.commit_url.split('/')[6]
        return format_html('<a href="{}" target="_blank">{}</a>',
                           obj.commit_url, commit)


admin.site.register(Commit, CommitAdmin)
