from app import db


class Carrito(db.Model):
    __tablename__ = 'carrito'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
     
    id_producto = db.Column(db.Integer, db.ForeignKey('products.id'), default = None)
    cantidad=db.Column(db.Integer, index=True, default=1)
    price = db.Column(db.Float, index=True, default=1)
    subtotal = db.Column(db.Float, index=True, default=1)
    #
    products = db.relationship('Product', back_populates='carrito')

    def __repr__(self):
        return f'Category: {self.name}' 

    def calcular_subtotal(self):
        self.subtotal = self.cantidad*self.price