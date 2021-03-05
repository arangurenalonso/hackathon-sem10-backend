from app import db


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True, default=None)
    status = db.Column(db.Integer, index=True, default=1)
    #
    products = db.relationship('Product', back_populates='category')

    def __repr__(self):
        return f'Category: {self.name}' 
