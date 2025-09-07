from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Natan Harum Panogu Silalahi',
        'npm' : '2406496170',
        'class': 'PBP E'
    }
    return render(request, "main.html", context)
