from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275784',
        'name': 'Dicky Bayu Sadewo',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
# Create your views here.
