from django.shortcuts import render
# from .models import productInfo


# products = [
#     {'a': 100, 'b': 200, 'c': 300},
#     {'c': 10, 'e': 20, 'f': 30},
#     {'g': 1, 'h': 2, 'i': 3}
# ]


def home(request):
    # context = {
    #     "products": products
    # }
    return render(request, "myhome/index.html")
