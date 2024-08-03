

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderdItem, Product
from .form import AddToCartForm
from django.contrib import messages
from .models import BillingAddress,Order
from .form import BillingAddressForm

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    customer = request.user.customer  # Assuming you have a Customer profile linked to the user
    order, created = Order.objects.get_or_create(owner=customer, order_status=Order.CART_STAGE)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            order_item = form.save(commit=False)
            order_item.owner = order
            order_item.product = product
            order_item.save()
            return redirect('cart')  # Redirect to the cart detail page
    else:
        form = AddToCartForm(initial={'product': product})

    return render(request, 'add_to_cart.html', {'form': form, 'product': product})


@login_required
def cart(request):
    customer = request.user.customer  # Assuming you have a Customer profile linked to the user
    order = Order.objects.filter(owner=customer, order_status=Order.CART_STAGE).first()
    return render(request, 'cart.html', {'order': order})


@login_required
def checkout(request):
    customer = request.user.customer  # Assuming you have a Customer profile linked to the user
    order = Order.objects.filter(owner=customer, order_status=Order.CART_STAGE).first()

    if not order:
        messages.error(request, "Your cart is empty.")
        return redirect('cart')
    # Calculate the total price of the order
    total_price = sum(item.product.price * item.quantity for item in order.added_items.all())

    try:
        billing_address = BillingAddress.objects.get(customer=request.user)
    except BillingAddress.DoesNotExist:
        messages.error(request, "Please provide your billing information.")
        return redirect('billing')

    # Here you would add any payment processing logic if applicable
    # For example, integrating with a payment gateway


    # Assuming payment is successful or not needed, update the order status
    if request.method == 'POST':
        form = BillingAddressForm(request.POST, instance=billing_address)
        if form.is_valid():
            billing_address = form.save(commit=False)
            billing_address.customer = request.user
            billing_address.save()
            order.order_status = Order.ORDER_CONFIRMED
            order.save()
            messages.success(request, "Your order has been successfully placed.")
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = BillingAddressForm(instance=billing_address)

        return render(request, 'checkout.html', {
        'order': order,
        'total_price': total_price,
        'billing_address': billing_address if billing_address else form,
    })
         

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, owner=request.user.customer)
    return render(request, 'order_confirmation.html', {'order': order})


@login_required
def billing(request):
    customer = request.user

    try:
        billing_address = BillingAddress.objects.get(customer=customer)
    except BillingAddress.DoesNotExist:
        billing_address = None

    if request.method == 'POST':
        form = BillingAddressForm(request.POST, instance=billing_address)
        if form.is_valid():
            billing_address = form.save(commit=False)
            billing_address.customer = customer
            billing_address.save()
            messages.success(request, 'Billing information saved successfully.')
            return redirect('order_confirmation.html')
    else:
        form = BillingAddressForm(instance=billing_address)

    return render(request, 'checkout.html', {'form': form})