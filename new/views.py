from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def post(request):
    return render(request, 'post.html')

def form(request):
    return render(request, 'forms.html')