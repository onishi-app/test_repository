from itertools import count
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "value": "Hello",
        "name": "Onishi"
    }
    return render(request, "TemplateApp/index.html", context)


def home(request, first_name, last_name):
    my_name = f"{first_name} {last_name}"
    favorite_fruits = ["Apple", "Grape", "Lemon"]
    my_info = {
        "name": "Taro",
        "age": 18
    }
    status = 20

    return render(request, "TemplateApp/home.html", context={
        "my_name": my_name, 
        "favorite_fluits": favorite_fruits,
        "my_info": my_info,
        "status": status
    })


def sample1(request):
    return render(request, "TemplateApp/sample1.html")


def sample2(request):
    return render(request, "TemplateApp/sample2.html")


def sample(request):
    name = "Onishi Ryosuke"
    height = 169.5
    weight = 56.4
    bmi = weight / (height / 100)**2
    page_url = "ホームページ: https://www.google.com"
    favorite_fruits = [
        "Apple", "Grape", "Lemon"
    ]
    msg = """hello
    my name is
    onishi
    """
    msg2 = "1234567890"
    return render(request, "TemplateApp/sample.html", context={
        "name": name,
        "bmi": bmi,
        "page_url": page_url,
        "fruits": favorite_fruits,
        "msg": msg,
        "msg2": msg2
    })


class Country:
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital


def sample3(request):
    country = Country("Japan", 100000000, "Tokyo")
    return render(request, "TemplateApp/sample3.html", context={
        "country": country
    })