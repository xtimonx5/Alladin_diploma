from django.contrib.admin import ModelAdmin
from django.http import HttpResponseRedirect

from management.models.company import Company
from management.models.farm import Farm
from management.models.animal import Animal
from django.contrib.admin import TabularInline, StackedInline
from django.core.urlresolvers import reverse
from django.utils.html import format_html


class FarmInline(TabularInline):
    def has_module_permission(self, request):
        return True

    def animals_count(self, obj):
        return Animal.objects.filter(farm=obj).count()

    def link(self, obj):
        url = reverse('admin:%s_%s_change' % (obj._meta.app_label,
                                              'farm'),
                      args=(obj.id,))
        return format_html(u'<a href="{}">{}</a>', (url), 'Change  ' + obj.name)

    readonly_fields = (
        'link',
        'name',
        'animals_count'
    )
    fields = (
        'link',
        'name',
        'animals_count',
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
    def changelist_view(self, request, extra_context=None):
        if not request.user.is_superuser:
            object_id = Company.objects.get(owner=request.user).id
            return HttpResponseRedirect(
                reverse(
                    'admin:%s_%s_change' % (self.opts.app_label, self.opts.model_name),
                    args=(object_id,),
                    current_app=self.admin_site.name
                )
            )
        else:
            return super(CompanyAdmin, self).changelist_view(request, extra_context)

    def farm_count(self, obj):
        return Farm.objects.filter(company=obj).count()

    list_display = ('name', 'farm_count')

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
