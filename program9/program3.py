import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='product123',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[],
    INSTALLED_APPS=['django.contrib.contenttypes'],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'products.db',
        }
    }
)

django.setup()

from django.http import HttpResponse
from django.urls import path

products = []

def home(request):
    html = """
    <h1>Product Management</h1>

    <form method="post" action="/add/">
        Product Name: <input type="text" name="name"><br><br>
        Price: <input type="number" name="price"><br><br>
        Quantity: <input type="number" name="quantity"><br><br>
        <button type="submit">Add Product</button>
    </form>

    <h2>Product List</h2>
    """

    for i, product in enumerate(products):
        html += f"""
        <p>
        <b>{product['name']}</b> -
        Price: {product['price']} -
        Quantity: {product['quantity']}
        <a href="/delete/{i}/">Delete</a>
        <a href="/detail/{i}/">View</a>
        </p>
        """

    return HttpResponse(html)

def add_product(request):
    if request.method == "POST":
        product = {
            "name": request.POST.get("name"),
            "price": request.POST.get("price"),
            "quantity": request.POST.get("quantity")
        }
        products.append(product)

    return home(request)

def detail(request, id):
    product = products[id]

    return HttpResponse(f"""
    <h1>Product Details</h1>
    <p>Product Name: {product['name']}</p>
    <p>Price: {product['price']}</p>
    <p>Quantity: {product['quantity']}</p>
    <a href="/">Back</a>
    """)

def delete_product(request, id):
    products.pop(id)
    return home(request)

urlpatterns = [
    path('', home),
    path('add/', add_product),
    path('detail/<int:id>/', detail),
    path('delete/<int:id>/', delete_product),
]

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program3.py",
        "runserver",
        "0.0.0.0:8003"
    ])