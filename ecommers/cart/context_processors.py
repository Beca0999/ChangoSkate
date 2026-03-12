from .cart import Cart

#Crear el contexto del carrito para que esté disponible en todas las plantillas
def cart(request):
    return {'cart': Cart(request)}