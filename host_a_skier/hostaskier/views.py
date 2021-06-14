from django.shortcuts import render
from .models import Post

hostinfo = [
    {
        'name': 'Bob Trueman',
        'price': "20 a set", 
        'location': "Vail, CO", 
        'avalibility': "anytime"
    },
        {
        'name': 'Pete Davidson',
        'price': "40 a set", 
        'location': "Squa Valley, CA", 
        'avalibility': "Mondays and Fridays"
    }
]


# Create your views here.
def home_view(request):
    context = {
        'hosts': Post.objects.all()
    }
    return render(request, 'hostaskier/home.html', context)

def about_view(request):
    return render(request, 'hostaskier/about.html')
