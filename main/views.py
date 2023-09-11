from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Devin Faiz Faturahman',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)