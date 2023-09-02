from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
# No shell
#python .\manage.py migrate
#python .\manage.py runserver