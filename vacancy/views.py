from django.shortcuts import render, HttpResponse, redirect
from .models import Company, Car, Renta

def index(request): 
    return render(request, 'home.html')

def company(request): 
    company = Company.objects.all()
    return render(request, 'company.html', {'companies': company})


def car_detail_view(request, pk): 
        company = Company.objects.filter(id=pk).first()
        car = Car.objects.filter(company=company)
        return render(request, 'car-detail.html', {'companies': company, 'cars': car})

def renta_create_view(request, pk): 
    if request.method=="GET":    
        car = Car.objects.filter(id=pk).first()
        renta = Renta.objects.filter(car=car)
        return render(request, 'renta-create.html', {'cars': car, 'renta': renta})
    elif request.method == "POST":
        car = request.POST.get('car', None)
        fullname = request.POST.get("fullname", None)
        age = request.POST.get("age", None)
        phone = request.POST.get("phone", None)
        email = request.POST.get("email", None)
        if not fullname or not age or not phone or not email:
            return HttpResponse("Fields are required!")
        car = Car.objects.get(id=pk)
        renta = Renta(fullname=fullname, age=age, phone=phone, email=email, car=car)
        renta.save()
        return redirect("/")

def renta_detail_view(request):
    renta = Renta.objects.select_related('car').all()
    return render(request, 'renta_detail_view.html', {'rentas': renta})    

def about(request): 
    return render(request, 'about.html')


def contact(request): 
    return render(request, 'contact.html')
