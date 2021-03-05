from app import db
from flask import url_for, redirect, flash
#from flask_login import current_user
from app.carrito.carritoModel import Carrito
from app.product.productModel import Product


class CarritoController:
    def __init__(self):
        pass#self.current_user = current_user

    def create(self, id_producto,cantidad):
        try:
            producto=Product.query.filter_by(id=id_producto).first()
            
            carrito = Carrito(  id_producto=id_producto, 
                                cantidad=cantidad, 
                                price=producto.price)
            carrito.calcular_subtotal()
            db.session.add(carrito)
            db.session.commit()
            flash('Se creo agrego el producto al carrito con exito !', 'success')
            return redirect(url_for('carrito'))
        except Exception as e:
            flash(f'Ocurrio un error -> {str(e)}', 'error')
            return redirect(url_for('carritoAdd'))

    def index(self, page, **kwargs):
        carrito = Carrito.query

        if kwargs['search']:
            carrito = carrito.filter(Carrito.products.name.ilike(f'%{kwargs["search"]}%'))


        carrito = carrito.order_by(Carrito.id).paginate(page, per_page=5, error_out=False)
        return carrito


    def delete(self, carrito_id):
        try:
            carrito = Carrito.query.filter_by(id=carrito_id).delete()
            db.session.commit()
            flash('Se Elimino el producto del carrito con exito !', 'success')
            return redirect(url_for('carrito'))
        except Exception as e:
            flash(f'Ocurrio un error -> {str(e)}', 'error')
            return redirect(url_for('carrito'))