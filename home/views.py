from django.shortcuts import render

# Create your views here.
def home(request):
    print('HOME')

    context = {
            "text": "Estamos na home"
        }

    return render(
        request,
        'home/home.html',
        context
    )