from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect
from .models import Order
from .forms import OrderForm, ItemForm


def order_list(request):
    qs = Order.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(store__icontains=q)

    return render(request, 'inventory_management/order_list.html', {
        'order_list': qs,
        'q':q,
    })

def order_detail(request, id):
    print(id)
    order = get_object_or_404(Order,id=id)
    return render(request, 'inventory_management/order_detail.html', {
        'order':order,
    })

def post_new(request):
    if request.method =='POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            # order = Order()
            # order.coffee_bean = form.cleaned_data['coffee_bean']
            # order.store = form.cleaned_data['store']
            # order.extra = form.cleaned_data['extra']
            # order.save()

            # order = Order(coffee_bean=form.cleaned_data['coffee_bean'],
            #               store=form.cleaned_data['store'],
            #               extra=form.cleaned_data['extra'])
            # order.save()
            #
            # order = Order.objects.create(coffee_bean=form.cleaned_data['coffee_bean'],
            #               store=form.cleaned_data['store'],
            #               extra=form.cleaned_data['extra'])

            # order = Order.objects.create(**form.cleaned_data)
            # 딕셔너리 언팩을 통해서 하는 방법.

            form.save()
            return redirect('inventory:order_list')
    else:
        form = OrderForm()
    return render(request, 'inventory_management/post_form.html', {
        'form':form,
    })


def item_new(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inventory:order_list')
    else:
        form = ItemForm()
    return render (request, 'inventory_management/post_form.html',{
        'form':form,
    })


def test(request):
    return render(request, 'index.html')