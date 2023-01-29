import decimal
from django.shortcuts import render
from .forms import PizzaForm
from django.contrib import messages
from .models import Pizza


def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    form = PizzaForm()
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save(commit=False)
            print('inside valid')
            size = form.cleaned_data.get('size')
            print(size)
            pizza_size_price = 4
            if size == 'Medium':
                pizza_size_price = 5.5
            elif size == 'Large':
                pizza_size_price = 7

            topping_list = form.cleaned_data.get('topping')
            print(topping_list)
            topping_prices = 0
            for topping in topping_list:
                print(topping.topping_price)
                print(topping_prices)
                topping_prices += topping.topping_price

            
            print(pizza.pizza_price)
            pizza.pizza_price = pizza_size_price + float(topping_prices)

            pizza.save()

            pizza_pk = pizza.id
            messages.success(request, 'Your order is on the way!')
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
            form.save()
            messages.success(request, 'Editted the pizza!')
        else:
            messages.warning(request, 'Something wrong!')
    context = {
        'form': form,
    }
    return render(request, 'pizza/edit_pizza.html', context)