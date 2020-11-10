from django.shortcuts import render


# Create your views here.
def view_bag(request):
    """ This view is rendering the bag contents page """
    return render(request, 'bag/bag.html')
