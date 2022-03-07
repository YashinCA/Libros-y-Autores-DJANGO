from django.shortcuts import render, HttpResponse, redirect, reverse

from .models import *


def index(request):
    if request.method == 'GET':
        context = {"authors": Authors.objects.all(),
                   "books": Book.objects.all()}
        return render(request, "books_authors_app/index.html", context)
    if request.method == "POST":
        print(request.POST)
        Book.objects.create(
            title=request.POST['titulo'], desc=request.POST['descripcion'])
        return redirect((reverse("bookauthor:book")))


def index_author(request):
    if request.method == 'GET':
        context = {"authors": Authors.objects.all(),
                   "books": Book.objects.all()}
        return render(request, "books_authors_app/author.html", context)
    if request.method == "POST":
        print(request.POST)
        Authors.objects.create(
            first_name=request.POST['nombre'], last_name=request.POST['apellido'], notas=request.POST['notas'])
        return redirect((reverse("bookauthor:author")))


def book_details(request, id_book):
    if request.method == 'GET':
        book_detail = Book.objects.get(id=id_book)
        autores_excl = Authors.objects.all().exclude(books=book_detail)
        context = {"book_det": book_detail,
                   "autores_det": book_detail.authors.all().order_by('id'),
                   "autores_excl": autores_excl
                   }
        return render(request, "books_authors_app/book_detail.html", context)

    if request.method == "POST":
        if request.POST['autores'] != '':
            book_detail = Book.objects.get(id=id_book)
            autores_excl = Authors.objects.all().exclude(books=book_detail)
            add_author = Authors.objects.get(id=request.POST['autores'])
            add_author.books.add(book_detail)
            context = {"book_det": book_detail,
                       "autores_det": book_detail.authors.all(),
                       "autores_excl": autores_excl
                       }
            return render(request, "books_authors_app/book_detail.html", context)
        else:
            book_detail = Book.objects.get(id=id_book)
            autores_excl = Authors.objects.all().exclude(books=book_detail)
            context = {"book_det": book_detail,
                       "autores_det": book_detail.authors.all(),
                       "autores_excl": autores_excl
                       }
            return render(request, "books_authors_app/book_detail.html", context)


def author_details(request, id_author):
    if request.method == 'GET':
        author_detail = Authors.objects.get(id=id_author)
        books_excl = Book.objects.all().exclude(authors=author_detail)
        context = {"author_det": author_detail,
                   "books_det": author_detail.books.all().order_by('id'),
                   "books_excl": books_excl
                   }
        return render(request, "books_authors_app/author_detail.html", context)

    if request.method == "POST":
        if request.POST['libros'] != '':
            print(request.POST['libros'])
            author_detail = Authors.objects.get(id=id_author)
            books_excl = Book.objects.all().exclude(authors=author_detail)
            add_book = Book.objects.get(id=request.POST['libros'])
            print(add_book)
            add_book.authors.add(author_detail)
            context = {"author_det": author_detail,
                       "books_det": author_detail.books.all().order_by('id'),
                       "books_excl": books_excl
                       }
            return render(request, "books_authors_app/author_detail.html", context)
        else:
            author_detail = Authors.objects.get(id=id_author)
            books_excl = Book.objects.all().exclude(authors=author_detail)
            context = {"author_det": author_detail,
                       "books_det": author_detail.books.all().order_by('id'),
                       "books_excl": books_excl
                       }
            return render(request, "books_authors_app/author_detail.html", context)
