class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')

        if not carro:
            carro=self.session['carro'] = {}
        #else:
        self.carro = carro


    def agregar(self, producto):
        if (str(producto.id) not in self.carro.keys()):
            self.carro[(producto.id)] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': str(producto.precio),
                'cantidad': 1,
                'imagen': producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if (str(producto.id) == key):
                    value['cantidad'] = value['cantidad'] + 1
                    value['precio'] = float(value['precio'])+producto.precio
                    break
        self.guardar()

    def guardar(self):
        self.session['carro'] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        if (str(producto.id) in self.carro.keys()):
            del self.carro[str(producto.id)]
            self.guardar()

    def restar(self, producto):
        if (str(producto.id) in self.carro.keys()):
            for key, value in self.carro.items():
                if (str(producto.id) == key):
                    if (value['cantidad'] >= 1):
                        value['cantidad'] = value['cantidad'] - 1
                        value['precio'] = float(value['precio'])-producto.precio
                        break
            self.guardar()

    def vaciar(self):
        self.session['carro'] = {}
        self.session.modified = True