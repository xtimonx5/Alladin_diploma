from django.contrib.admin import ModelAdmin
from management.models.company import Company
from management.models.farm import Farm
from django.contrib.admin import TabularInline, StackedInline
from django.core.urlresolvers import reverse
from django.utils.html import format_html


class FarmInline(StackedInline):
    def has_module_permission(self, request):
        return True

    def link(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label,
                                              'farm'),
                      args=(obj.id,))
        return format_html(u'<a href="{}">{}</a>', (url), 'Change  ' + obj.name)

    readonly_fields = (
        'link',
    )
    fields = (
        'link',
        'name',
    )

    model = Farm
    extra = 0

    def has_change_permission(self, request, obj=None):
        return True

        # def has_delete_permission(self, request, obj=None):
        #     return True

        # def has_add_permission(self, request):
        #     return True


class CompanyAdmin(ModelAdmin):
    # def get_list_display(self, request):
    #     if request.user.is_superuser:
    #         return super(CompanyAdmin, self).get_list_display(request)
    #     else:
    #         obj = Company.objects.get(owner=request.user)
    #         url = reverse('admin:%s_%s_change' % (obj._meta.app_label,
    #                                               'company'),
    #                       args=(obj.id,))
    #         return

    inlines = [
        FarmInline,
    ]

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Company.objects.all()
        else:
            return Company.objects.filter(owner=request.user)

    def has_module_permission(self, request):
        return True

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return True

    class Meta:
        model = Company
