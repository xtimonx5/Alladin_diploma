from django.shortcuts import render, render_to_response

# Create your views here.
from management.models.animal import Animal
from management.models.animal_type import AnimalType
from management.models.company import Company
from management.models.farm import Farm
from management.models.farm_group import FarmGroup
from management.models.norm import Norm


def redirect_to_render_report(group_id):
    pass


def rasschet_view(request):
    parent = request.GET.get('parent', None)
    user = request.user
    company = Company.objects.filter(owner=user)
    context = {}
    context['company'] = company
    farms = Farm.objects.filter(company=company)
    context['farms'] = farms
    if parent:
        context['groups'] = FarmGroup.objects.filter(farm_id=parent)
        if context['groups'].exists():
            context['farms'] = farms.filter(id=parent)
    group = request.GET.get('group', None)
    if group:
        redirect_to_render_report(group)
    return render_to_response(template_name='rasschet.html', context=context)
