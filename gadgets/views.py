from django.shortcuts import render, get_object_or_404
from .models import gadgetAttr


def viewGadgets(request):
    gadgets = gadgetAttr.objects.all()

    context = {
        'gadgets': gadgets

    }
    return render(request, 'gadgets/view_gadgets.html', context)


def viewGadgetDetail(request, gadget_id):
    gadget = get_object_or_404(gadgetAttr, asins='gadget_id')

    context = {
        'gadget': gadget

    }
    return render(request, 'gadgets/gadget_details.html', context)
