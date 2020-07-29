from django.shortcuts import render
from .models import Product
from datetime import datetime, timedelta
from .filters import ProductFilter



# Create your views here.

def index(request):

    products = Product.objects.all()

    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs

    best_sell = Product.objects.filter(labels='Best Sellers')
    Features = Product.objects.filter(labels='Features')

    one_week_ago = datetime.today() - timedelta(days=7)
    week_deals = Product.objects.filter(date_created__gte=one_week_ago)[:4]



    context = {
        'products': products,
        'best_sell': best_sell,
        'Features': Features,
        'week_deals': week_deals,
        'myFilter': myFilter
    }
    return render(request,'index.html', context)



def cart(request):
    return render(request, 'cart_page.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact_us.html')

def checkout(request):
    return render(request, 'checkout_page.html')

def product_details(request):
    return render(request, 'product_detail_page.html')

def shop(request):
    return render(request, 'category_page.html')
