from app import db
 
 
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True, default=None)
    price = db.Column(db.Float, index=True, default=1)
    stock = db.Column(db.Integer, index=True, default =1)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), default = None)
    status = db.Column(db.Integer, index=True, default=1)
    #
    category = db.relationship('Category', back_populates='products')
    carrito = db.relationship('Carrito', back_populates='products')
    def __repr__(self):
        return f'Product: {self.name}'


