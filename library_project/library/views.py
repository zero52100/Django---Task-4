
from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Book
from .models import Author

from .models import Book

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})

class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)  
    return render(request, 'library/book_detail.html', {'book': book})