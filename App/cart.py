class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            self.session["cart"] = {}
            self.cart = self.session["cart"]
        else:
            self.cart = cart

    def add_service(self, service):
        id = str(service.id)
        if id not in self.cart.keys():
            self.cart[id]={
                "service_id": service.id,
                "name": service.name,
                "price": service.price,
                "accumulated": service.price,
                "amount": 1,
            }
        else:
            self.cart[id]["amount"] += 1
            self.cart[id]["price"] = service.price
            self.cart[id]["accumulated"] += service.price
        self.save_cart()

    def save_cart(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def delete_service(self, service):
        id = str(service.id)
        if id in self.cart:
            del self.cart[id]
            self.save_cart()

    def subtract(self, service):
        id = str(service.id)
        if id in self.cart.keys():
            self.cart[id]["amount"] -= 1
            self.cart[id]["accumulated"] -= service.price
            if self.cart[id]["amount"] <= 0: self.delete_service(service)
            self.save_cart()

    def clean(self):
        self.session["cart"] = {}
        self.session.modified = True