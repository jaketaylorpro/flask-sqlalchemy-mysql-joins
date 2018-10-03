from . import db
from util import dict_to_json


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(80), unique=True)
    subscriptions = db.relationship("Subscription", backref="user")

    def to_json(self):
        return dict_to_json(
            self.asdict(
                exclude_pk=True,
                follow={'subscriptions': {
                    'exclude': ['id', 'product_id', 'user_id'],
                    'follow': {'product': {'exclude_pk': True}}}}))
