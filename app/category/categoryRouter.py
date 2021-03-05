from app import app
from flask import render_template, request
#from flask_login import login_required
from app.category.categoryController import CategoryController
from app.category.categoryForm import CategoryForm
from app.category.categoryModel import Category

 
@app.route('/categories')
#@login_required
def categories():
    page = request.args.get('page', type=int, default=1)
    search = request.args.get('search', type=str, default='')
    controller = CategoryController()
    categories = controller.index(page=page, search=search)
    return render_template('views/categories/index.html', 
                        title='Categorias', data=categories, search=search)


@app.route('/categories/create', methods=['GET', 'POST'])
#@login_required
def categories_create():
    form = CategoryForm()
    if form.validate_on_submit():
        controller = CategoryController()
        return controller.create(form)
    return render_template('views/categories/form/create.html', title='Categorias', form=form)


@app.route('/categories/update/<int:id>', methods=['GET', 'POST'])
#@login_required
def categories_update(id):
    pass
    categoria = Category.query.get_or_404(id)
    form = CategoryForm(obj=categoria)
    if form.validate_on_submit():
        controller = CategoryController()
        return controller.update(form, id)
    return render_template('views/categories/form/update.html', title='Categorias', form=form)


@app.route('/categories/delete/<int:id>', methods=['GET', 'POST'])
#@login_required
def categories_delete(id): 
    controller = CategoryController()
    return controller.delete(id)


##################################################
#               Luego cambiar
##################################################
@app.route('/index', methods=['GET', 'POST'])
#@login_required
def index(): 
    return 'index'

@app.route('/logout', methods=['GET', 'POST'])
#@login_required
def logout(): 
    return 'logout'