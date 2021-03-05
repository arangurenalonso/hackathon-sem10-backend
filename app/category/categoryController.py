from app import db
from flask import url_for, redirect, flash
#from flask_login import current_user
from app.category.categoryModel import Category


class CategoryController:
    def __init__(self):
        pass#self.current_user = current_user

    def index(self, page, **kwargs):
        categories = Category.query

        if kwargs['search']:
            categories = categories.filter(Category.name.ilike(f'%{kwargs["search"]}%'))

        categories = categories.order_by(Category.id).paginate(page, per_page=5, error_out=False)
        return categories

    def create(self, form):
        try:
            category = Category(name=form.name.data, status=1)
            db.session.add(category)
            db.session.commit()
            flash('Se creo la categoria con exito !', 'success')
            return redirect(url_for('categories'))
        except Exception as e:
            flash(f'Ocurrio un error -> {str(e)}', 'error')
            return redirect(url_for('categories_create'))

    def update(self, form, category_id):
        try:
            category = Category.query.filter_by(id=category_id).first()
            category.name = form.name.data
            db.session.commit()
            flash('Se actualizo la categoria con exito !', 'success')
            return redirect(url_for('categories'))
        except Exception as e:
            flash(f'Ocurrio un error -> {str(e)}', 'error')
            return redirect(url_for('categories_update', id=category_id))

    def delete(self, category_id):
        try:
            category = Category.query.filter_by(id=category_id).first()
            status = category.status
            if status == 1:
                status = 0
            else:
                status = 1
            category.status = status
            db.session.commit()
            flash('Se actualizo la categoria con exito !', 'success')
            return redirect(url_for('categories'))
        except Exception as e:
            flash(f'Ocurrio un error -> {str(e)}', 'error')
            return redirect(url_for('categories'))
