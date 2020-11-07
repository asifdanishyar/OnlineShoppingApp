from django.shortcuts import render

# Create your views here.
def index(request):
    """ This view returns index page from home """
    return render(request, 'home/index.html')
