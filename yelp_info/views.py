from django.shortcuts import render

def get_template(request):
    return render(request, 'base.html')
