from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from intranet.serializers import BookSerializer
from intranet.models import Book
from django.contrib.auth.decorators import login_required


def index(request):
    books = Book.objects.all()
    context = {
        "books": books,  # Pass the queried data to the template
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


# def book(request) -> HttpResponse:
#     template = loader.get_template('book.html')
#     return HttpResponse(template.render())


def login(request):
    return render(request, "registration/login.html")


#def register(request):
#    form_class = UserCreationForm
#    success_url = reverse_lazy("login")
#    template_name = "registration/register.html"
#    return render(request, "registration/register.html")


@login_required
def watchvideos(request):
    return render(request, "watchvideos.html")

def handler404(request, exception=None):
    return render(
        request, 
        'bad_request.html')
    

def handler500(request):
    return render(request, 'server_error.html', status=500)