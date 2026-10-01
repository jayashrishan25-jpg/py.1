from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY="123",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[]
)

import django
django.setup()

from django.http import HttpResponse
from django.urls import path

books = []

def home(request):
    html = """
    <h1>Book Management</h1>

    <form method="post" action="/add/">
    Book Name: <input name="name"><br><br>
    Author: <input name="author"><br><br>
    <button>Add Book</button>
    </form><hr>
    """

    for i, b in enumerate(books):
        html += f"""
        <h3>{b['name']}</h3>
        <p>Author: {b['author']}</p>
        <a href="/edit/{i}/">Edit</a> |
        <a href="/delete/{i}/">Delete</a>
        """

    return HttpResponse(html)

def add(request):
    if request.method == "POST":
        books.append({
            "name": request.POST["name"],
            "author": request.POST["author"]
        })
    return home(request)

def edit(request, id):
    if request.method == "POST":
        books[id]["name"] = request.POST["name"]
        books[id]["author"] = request.POST["author"]
        return home(request)

    b = books[id]

    return HttpResponse(f"""
    <form method="post">
    Book Name: <input name="name" value="{b['name']}"><br><br>
    Author: <input name="author" value="{b['author']}"><br><br>
    <button>Update</button>
    </form>
    """)

def delete(request, id):
    books.pop(id)
    return home(request)

urlpatterns = [
    path("", home),
    path("add/", add),
    path("edit/<int:id>/", edit),
    path("delete/<int:id>/", delete)
]

from django.core.management import execute_from_command_line

execute_from_command_line([
    "program.py", "runserver", "0.0.0.0:8005"
])