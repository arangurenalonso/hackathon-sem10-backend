from app import db
from flask import url_for, redirect, flash
#from flask_login import current_user
from app.product.productModel import Product

 
class ProductController:
    def __init__(self):
        pass
        #self.current_user = current_user

    def index(self, page, **kwargs):
        products = Product.query

        if kwargs['search']:
            products = products.filter(Product.name.ilike(f'%{kwargs["search"]}%'))

        if kwargs['category']:
            products = products.filter(Product.category_id == kwargs['category'] )

        products = products.order_by(Product.id).paginate(page, per_page=5, error_out=False)
        return products

    def create(self, form):
        try:
            products = Product(name=form.name.data, 
                                stock=form.stock.data, 
                                price=form.price.data, 
                                category_id=form.category_id.data, 
                                status=1)
            db.session.add(products)
            db.session.commit()
            flash('Se creo el producto con exito !', 'success')
            return redirect(url_for('products'))
        except Exception as e:
            flash(f'Ocurrio un error -> {str(e)}', 'error')
            return redirect(url_for('products_create'))

    def update(self, form, product_id):
        try:
            product = Product.query.filter_by(id=product_id).first()
            product.name = form.name.data
            product.stock = form.stock.data
            product.price = form.price.data
            product.category_id = form.category_id.data
            
            db.session.commit()
            flash('Se actualizo el producto con exito !', 'success')
            return redirect(url_for('products'))
        except Exception as e:
            flash(f'Ocurrio un error -> {str(e)}', 'error')
            return redirect(url_for('products_update', id=product_id))

    def delete(self, product_id):
        try:
            product = Product.query.filter_by(id=product_id).first()
            status = product.status
            if status == 1:
                status = 0
            else:
                status = 1
            product.status = status
            db.session.commit()
            flash('Se actualizo el producto con exito !', 'success')
            return redirect(url_for('products'))
        except Exception as e:
            flash(f'Ocurrio un error -> {str(e)}', 'error')
            return redirect(url_for('products'))
