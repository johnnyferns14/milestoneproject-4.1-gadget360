from django.shortcuts import render
from .models import gadgetAttr


def viewGadgets(request):
 
    gadgets = gadgetAttr.objects.all()

    context = {
        'gadgets': gadgets

    }
    return render(request, 'gadgets/view_gadgets.html', context)
