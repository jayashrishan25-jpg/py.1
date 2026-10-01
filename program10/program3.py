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

products = []

def home(request):
    html = """
    <h1>Product Management</h1>

    <form method="post" action="/add/">
    Product: <input name="name"><br><br>
    Price: <input name="price"><br><br>
    <button>Add Product</button>
    </form><hr>
    """

    for i, p in enumerate(products):
        html += f"""
        <h3>{p['name']}</h3>
        <p>Price: ₹{p['price']}</p>
        <a href="/edit/{i}/">Edit</a> |
        <a href="/delete/{i}/">Delete</a>
        """

    return HttpResponse(html)

def add(request):
    if request.method == "POST":
        products.append({
            "name": request.POST["name"],
            "price": request.POST["price"]
        })
    return home(request)

def edit(request, id):
    if request.method == "POST":
        products[id]["name"] = request.POST["name"]
        products[id]["price"] = request.POST["price"]
        return home(request)

    p = products[id]

    return HttpResponse(f"""
    <form method="post">
    Product: <input name="name" value="{p['name']}"><br><br>
    Price: <input name="price" value="{p['price']}"><br><br>
    <button>Update</button>
    </form>
    """)

def delete(request, id):
    products.pop(id)
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