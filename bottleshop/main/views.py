from django.shortcuts import render
from .models import (
    Banner,
    Category,
    Brand,
    ProductAttribute,
    Product,
    Color,
    Size,
)

# Create your views here.
def home(request):
    return render(request, "index.html")
