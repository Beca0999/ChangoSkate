from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_products(self):
        # Obtener los IDs de los productos en el carrito
        products_ids =  self.cart.keys()
        #Uso de los productos en el carrito para obtener los objetos Product correspondientes
        products = Product.objects.filter(id__in=products_ids)
        return products
    
    def get_quantities(self):
        quantities = self.cart
        return quantities
        