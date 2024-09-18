from django.urls import path
from . import views
from intranet.viewsa.book import add_update_book, book, get_all_books, readbook
from rest_framework.schemas import get_schema_view

import intranet
schema_view = get_schema_view(
    title='YeneTech API Docs',
    urlconf='intranet.urls'
)


urlpatterns = [
    path("about/", views.about, name="about"),  # Define a URL pattern for /about
    path("", views.index, name="index"),  # Example for homepage
    path(
        "contact/", views.contact, name="contact"
    ),  # Define a URL pattern for /contact
    path("book/", book, name="book"),  # Define a URL pattern for /book
    path("login/", views.login, name="login"),  # Define a URL pattern for /login
    #path(
    #    "register/", views.register, name="register"
     #),  # Define a URL pattern for /register
    # path(
    #     "watchvideos/", views.login, name="watchvideos"
    # ),  # Define a URL pattern for /watchvideos
     path('book/read/<int:book_id>/', readbook, name='read-books'),
    # # Other URL patterns
    path(r'api/', get_all_books),
    path(r'api/add-update', add_update_book),
    path('api/', schema_view),
]
