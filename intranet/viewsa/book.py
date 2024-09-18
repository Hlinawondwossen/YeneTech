from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from intranet.serializers import BookSerializer
from intranet.models import Book
from django.contrib.auth.decorators import login_required
from drf_yasg.utils import swagger_auto_schema


@api_view(['GET'])
def book(request):
    # Query the database for all books
    books = Book.objects.all()
    context = {
        "books": books,  # Pass the queried data to the template
    }
    return render(request, "book.html", context)

@api_view(['GET'])
def get_all_books(request, format=None):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put', 'post'], request_body=BookSerializer)
@api_view(['PUT', 'POST'])
def add_update_book(request, pk=None, format=None):
    if request.method == 'POST':
        # Create a new book
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        # Update an existing book
        try:
            book = Book.objects.get(pk=pk)  # Get the book by primary key (ID)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        # Partial update using the validated data
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # Save the updated book
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required
def readbook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "readbooks.html", {"book": book})
