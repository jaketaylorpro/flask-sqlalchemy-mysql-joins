from . import api
from ..db.product import Product


@api.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
    print('loading product: ' + str(product_id))
    product = Product.query.filter_by(id=product_id).first()
    return product.to_json()

