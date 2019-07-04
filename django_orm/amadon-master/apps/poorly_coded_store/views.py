from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    request.session.flush()
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    product = Product.objects.get(id=request.POST['id'])
    price_from_form = product.price
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    request.session["order"] = order.id
    
    return redirect("/checkout_page")

def checkout_page(request):
    if 'order' not in request.session:
        return redirect('/')

    current_order = Order.objects.get(id=request.session['order'])
    all_orders = Order.objects.all()
    total_charge = 0
    total_quantity = 0

    for order in all_orders:
        total_charge += order.total_price
        total_quantity += order.quantity_ordered

    context = {
        'current_order' : current_order,
        'total_charge' : total_charge,
        'total_quantity' : total_quantity
    }


    return render(request, "store/checkout.html",context)