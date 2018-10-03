from . import api
from ..db import db
from ..db.product import Product
from flask import request


@api.route('/product', methods=['POST'])
def add_product():
    product = Product()
    product.fromdict(request.json)
    db.session.add(product)
    db.session.commit()
    return '', 201
