
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderdItem, Product
from .form import AddToCartForm
from .models import Order
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .form import BillingInformationForm
from .models import Order, BillingInformation
from customers . models import Customer
from decimal import Decimal


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    customer = request.user.customer  # Assuming the user has a related Customer profile

    # Get or create an active order for the customer
    order, created = Order.objects.get_or_create(owner=customer, order_status=Order.CART_STAGE)

    # Check if the product is already in the cart
    order_item, created = OrderdItem.objects.get_or_create(owner=order, product=product)

    if not created:
        # If the item is already in the cart, increase the quantity
        order_item.quantity += 1
        order_item.save()
    else:
        # If the item is not in the cart, set the quantity to 1 (this may already be the default)
        order_item.quantity = 1
        order_item.save()

    # Redirect to the cart summary page or any other relevant page
    return redirect('cart')


@login_required
def cart(request):
    customer = request.user.customer  # Assuming you have a Customer profile linked to the user
    order = Order.objects.filter(owner=customer, order_status=Order.CART_STAGE).first()


    context = {
        'order':order,
    }
    return render(request, 'cart.html',context)





@login_required
def checkout(request):
    customer = request.user.customer
    order = get_object_or_404(Order, owner=customer, order_status=Order.CART_STAGE)
    if request.method == 'POST':
        form = BillingInformationForm(request.POST)
        if form.is_valid():
            billing_info = form.save(commit=False)
            billing_info.customer = customer
            billing_info.save()
            # Update order status to confirmed
            order.order_status = Order.ORDER_CONFIRMED
            order.save()
            return redirect('checkout_success')
    else:
        form = BillingInformationForm()
    return render(request, 'checkout.html', {'form': form, 'order': order})

@login_required
def checkout_success(request):
    return render(request, 'checkout_success.html')



def remove_from_cart(request, item_id):
    # Assuming that request.user is a Django User instance, and you have a ForeignKey from Customer to User.
    customer = get_object_or_404(Customer, user=request.user)
    
    # Fetch the current order.
    order = Order.objects.get(owner=customer, order_status=Order.CART_STAGE)
    
    # Get the item to be removed.
    item = get_object_or_404(OrderdItem, id=item_id, owner=order)
    
    # Delete the item from the order.
    item.delete()
    
    # Redirect to the cart detail view or any other view as needed.
    return redirect('cart')  # Replace 'cart_detail' with your cart page's URL name.


