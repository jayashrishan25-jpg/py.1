import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='patient123',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[],
    INSTALLED_APPS=['django.contrib.contenttypes'],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'patients.db',
        }
    }
)

django.setup()

from django.http import HttpResponse
from django.urls import path

patients = []

def home(request):
    html = """
    <h1>Patient Record Management</h1>

    <form method="post" action="/add/">
        Name: <input type="text" name="name"><br><br>
        Age: <input type="number" name="age"><br><br>
        Disease: <input type="text" name="disease"><br><br>
        <button type="submit">Add Patient</button>
    </form>

    <h2>Patient List</h2>
    """

    for i, patient in enumerate(patients):
        html += f"""
        <p>
        <b>{patient['name']}</b> -
        Age: {patient['age']} -
        Disease: {patient['disease']}
        <a href="/delete/{i}/">Delete</a>
        <a href="/detail/{i}/">View</a>
        </p>
        """

    return HttpResponse(html)

def add_patient(request):
    if request.method == "POST":
        patient = {
            "name": request.POST.get("name"),
            "age": request.POST.get("age"),
            "disease": request.POST.get("disease")
        }
        patients.append(patient)

    return home(request)

def detail(request, id):
    patient = patients[id]

    return HttpResponse(f"""
    <h1>Patient Details</h1>
    <p>Name: {patient['name']}</p>
    <p>Age: {patient['age']}</p>
    <p>Disease: {patient['disease']}</p>
    <a href="/">Back</a>
    """)

def delete_patient(request, id):
    patients.pop(id)
    return home(request)

urlpatterns = [
    path('', home),
    path('add/', add_patient),
    path('detail/<int:id>/', detail),
    path('delete/<int:id>/', delete_patient),
]

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line([
        "program4.py",
        "runserver",
        "0.0.0.0:8002"
    ])