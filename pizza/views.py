from django.shortcuts import render
from .forms import PizzaForm
from django.contrib import messages
from .models import Pizza, Size, Topping


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    form = PizzaForm()
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save(commit=False)

            size = form.cleaned_data.get('size')
            size_price = Size.objects.get(name=size).size_price

            topping_list = form.cleaned_data.get('topping')
            topping_prices = 0
            for topping in topping_list:
                topping_price = Topping.objects.get(name=topping).topping_price
                topping_prices += topping_price

            pizza_price = size_price + topping_prices
            
            pizza.pizza_price = pizza_price
            pizza.save()
            
            pizza_pk = pizza.id

            name = form.cleaned_data.get('customer_name')
            messages.success(request, f'Thank you {name.title()}, your order is on the way! You will pay ${pizza_price}.')
            form = PizzaForm()
        else:
            messages.warning(request, 'Something wrong!')
            pizza_pk = None
        context = {
            'form': form,
            'pizza_pk': pizza_pk,
        }
        return render(request, 'pizza/order.html', context)
    context = {
        'form': form,
    }
    return render(request, 'pizza/order.html', context)


def edit_order(request, id):
    pizza = Pizza.objects.get(id=id)
    form = PizzaForm(instance=pizza)
    if request.method == 'POST':
        form = PizzaForm(request.POST, instance=pizza)
        if form.is_valid():

            # There must be a code here to update the price!!!!!
            form.save()

            messages.success(request, 'Editted the pizza!')
        else:
            messages.warning(request, 'Something wrong!')
    context = {
        'form': form,
    }
    return render(request, 'pizza/edit_pizza.html', context)