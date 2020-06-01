import json
from .models import *


def cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    print('Cart:', cart)
    products = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            print(total)
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            product = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,
                    'price': product.price,
                    'image_url': product.image_url,
                },
                'quantity': cart[i]['quantity'],
                'get_total': total
            }
            products.append(product)
        except:
            pass
    return {'cartItems': cartItems, 'order': order, 'products': products}


def cart_data(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        products = order.orderproduct_set.all()
        cartItems = order.get_cart_items

    else:
        cookie_data = cookie_cart(request)
        products = cookie_data['products']
        order = cookie_data['order']
        cartItems = cookie_data['cartItems']
    return {'cartItems': cartItems, 'order': order, 'products': products}


def guest_order(request, data):
    print("User is not authenticated")
    print('COOKIES:', request.COOKIES)

    firstname = data['shipping-info']['firstname']
    email = data['shipping-info']['email']

    cookie_data = cookie_cart(request)
    products = cookie_data['products']

    customer, created = Customer.objects.get_or_create(
        email=email,
    )

    customer.name = firstname
    customer.save()

    order = Order.objects.create(
        customer=customer,
        completed=False,
    )
    for item in products:
        product = Product.objects.get(id=item['product']['id'])

        order_product, created = OrderProduct.objects.get_or_create(
            product=product,
            order=order,
            quantity=item['quantity'],
        )
        order_product.save()

    return customer, order

