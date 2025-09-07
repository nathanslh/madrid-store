from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406496170',
        'name': 'Natan Harum Panogu Silalahi',
        'class': 'PBP E'
    }
    return render(request, "main.html", context)
