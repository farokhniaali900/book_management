from django.shortcuts import render , get_object_or_404 , redirect
from .forms import BookForm
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request , 'books/book_list.html' , {'books' : books})


def book_detail(request , pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request , 'books/book_detail.html' , {'book':book})


def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    
    else:
        form = BookForm()
    return render(request , 'books/book_form.html' , {'form' : form})


def book_edit(request , pk):
    book = get_object_or_404(Book , pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST , instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request , 'books/book_form.html' , {'form' : form})


def book_delete(request , pk):
    book = get_object_or_404(Book , pk=pk)
    book.delete()
    return redirect('book_list')


def book_search(request):
    query = request.GET.get('search_for')
    results = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    return render(request , 'books/book_list.html' , {'books' : results})


def filter(request):
    price = request.GET.get('price')
    publication_date = request.GET.get('publication_date')
    publication_date_before = request.GET.get('publication_date_before')
    books = Book.objects.all()

    if price:
        books = books.filter(price__lte=price)
    if publication_date:
        books = books.filter(publication_date__gte=publication_date)
    if publication_date_before:
        books = books.filter(publication_date__lte=publication_date_before)

    return render(request , 'books/book_list.html' , {'books' : books})


def book_filter_delete(request):
    price = request.GET.get('price')
    publication_date = request.GET.get('publication_date')
    books = Book.objects.all()

    if price:
        books = books.filter(price__lte=price)
    if publication_date:
        books = books.filter(publication_date__gte=publication_date)

    books.delete()
    return redirect('book_list')