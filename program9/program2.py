import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='library123',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[],
    INSTALLED_APPS=['django.contrib.contenttypes'],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'library.db',
        }
    }
)

django.setup()

from django.http import HttpResponse
from django.urls import path

books = []

def home(request):
    html = """
    <h1>Library Book Management</h1>

    <form method="post" action="/add/">
        Book Name: <input type="text" name="name"><br><br>
        Author: <input type="text" name="author"><br><br>
        Price: <input type="number" name="price"><br><br>
        <button type="submit">Add Book</button>
    </form>

    <h2>Book List</h2>
    """

    for i, book in enumerate(books):
        html += f"""
        <p>
        <b>{book['name']}</b> -
        Author: {book['author']} -
        Price: {book['price']}
        <a href="/delete/{i}/">Delete</a>
        <a href="/detail/{i}/">View</a>
        </p>
        """

    return HttpResponse(html)

def add_book(request):
    if request.method == "POST":
        book = {
            "name": request.POST.get("name"),
            "author": request.POST.get("author"),
            "price": request.POST.get("price")
        }
        books.append(book)

    return home(request)

def detail(request, id):
    book = books[id]

    return HttpResponse(f"""
    <h1>Book Details</h1>
    <p>Book Name: {book['name']}</p>
    <p>Author: {book['author']}</p>
    <p>Price: {book['price']}</p>
    <a href="/">Back</a>
    """)

def delete_book(request, id):
    books.pop(id)
    return home(request)

urlpatterns = [
    path('', home),
    path('add/', add_book),
    path('detail/<int:id>/', detail),
    path('delete/<int:id>/', delete_book),
]

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program2.py",
        "runserver",
        "0.0.0.0:8002"
    ])