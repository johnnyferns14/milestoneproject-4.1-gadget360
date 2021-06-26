from django.shortcuts import render


def productReview(request):

    return render(request, 'reviews/reviews.html')
