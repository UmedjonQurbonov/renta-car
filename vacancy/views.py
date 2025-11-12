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
    car = Car.objects.get(id=pk)

    if request.method == "GET":    
        return render(request, 'renta-create.html', {'car': car})
    
    elif request.method == "POST":
        fullname = request.POST.get("fullname")
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        days = request.POST.get("days")

        if not fullname or not age or not phone or not email or not days:
            return HttpResponse("Все поля обязательны!")

        days = int(days)
        total_price = car.price_per_day * days

        renta = Renta(
            fullname=fullname,
            age=age,
            phone=phone,
            email=email,
            car=car,
            days=days,
            total_price=total_price
        )
        renta.save()
        return redirect("/")
    
    return render(request, 'renta-create.html', {'car': car})


def renta_detail_view(request):
    renta = Renta.objects.select_related('car').all()
    return render(request, 'renta_detail_view.html', {'rentas': renta})    

def about(request): 
    return render(request, 'about.html')


def contact(request): 
    return render(request, 'contact.html')
