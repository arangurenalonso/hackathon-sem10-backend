from app import app
from flask import render_template, request, flash, redirect,url_for
#from flask_login import login_required
from app.product.productController import ProductController
from app.product.productForm import ProductForm
from app.product.productModel import Product
from app.category.categoryModel import Category
from app.carrito.carritoModel import Carrito
from app.carrito.carritoController import CarritoController
 

@app.route('/carrito/add')
#@login_required
def carritoAdd():
    page = request.args.get('page', type=int, default=1)
    search = request.args.get('search', type=str, default='')
    category = request.args.get('category', type=int, default='')
    cantidad = request.args.get('cantidad', type=int, default='')
    id_producto = request.args.get('product_id', type=int, default='')

    if id_producto != "":
        if cantidad  =="":
            flash('Es necesario ingresar una cantidad que necesita agregar al carrito')
            return redirect(url_for('carritoAdd'))
        if Carrito.query.filter_by(id_producto=id_producto).first():
            flash('El producto ya ha sido agregado al carrito')
            return redirect(url_for('carritoAdd'))
        controller = CarritoController()
        return controller.create(id_producto,cantidad)

    categories = Category.query.filter_by(status=1).order_by(Category.name).all()

    controller = ProductController()
    products = controller.index(page=page, search=search, category = category)

    return render_template('views/carrito/carritoAdd.html', 
                        title='Agregar Carrito', data=products, search=search, categories = categories, category = category)


@app.route('/carrito', methods=['GET', 'POST'])
#@login_required
def carrito():
    page = request.args.get('page', type=int, default=1)
    search = request.args.get('search', type=str, default='')
    cantidad = request.args.get('cantidad', type=int, default='')
    
    controller = CarritoController()
    carrito = controller.index(page=page, search=search)
    
    total = sum([c.subtotal for c in carrito.items] )
    return render_template('views/carrito/index.html', 
                        title='CARRITO DE COMPRAS', data=carrito,search=search, total=total)

@app.route('/carrito/delete/<int:id>', methods=['GET', 'POST'])
#@login_required
def carrito_delete(id):
    controller = CarritoController()
    return controller.delete(id)