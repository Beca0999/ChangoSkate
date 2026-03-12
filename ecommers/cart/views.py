from django.shortcuts import redirect, render, get_object_or_404
from .cart import Cart 
from store.models import Product
from django.http import JsonResponse
# Create your views here.
def cart(request):
    cart = Cart(request)
    cart_products = cart.get_products
    quantities = cart.get_quantities
    return render(request, 'cart.html', {"cart_products": cart_products, "quantities": quantities})

def cart_add(request):
    # Leer el ID desde POST, no desde la URL
    product_id = request.POST.get('product_id')
    product_qty = request.POST.get('product_qty')  
    if not product_id:
        return JsonResponse({'message': 'product_id no enviado'}, status=400)

    try:
        product_id = int(product_id)
    except ValueError:
        return JsonResponse({'message': 'product_id inválido'}, status=400)

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    

    cart.add(product=product, quantity=product_qty)  
    # Obtener la cantidad total de productos en el carrito
    cart_quantity = cart.__len__()
    response = JsonResponse({
        'qty': cart_quantity
    }) 
    return response

def cart_delete(request, product_id):      
    # Lógica para eliminar el producto del carrito
    pass
def cart_update(request, product_id):    
    # Lógica para actualizar la cantidad del producto en el carrito
    pass

def cart_clear(request):    
    # Lógica para vaciar el carrito
    pass