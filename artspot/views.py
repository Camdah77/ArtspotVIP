from django.shortcuts import render, HttpResponse

# HTML- pages
def landing_page(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'index.html')  
def about(request):
    return render(request, 'about.about.html')  