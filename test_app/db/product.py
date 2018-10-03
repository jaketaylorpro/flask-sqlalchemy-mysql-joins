from util import dict_to_json
from . import db


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def to_json(self):
        return dict_to_json(
            self.asdict(
                exclude_pk=True))
