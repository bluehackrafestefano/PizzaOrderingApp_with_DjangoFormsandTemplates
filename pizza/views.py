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
            pizza = form.save()
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