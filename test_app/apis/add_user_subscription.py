from ..db.subscription import Subscription
from . import api
from ..db import db
from flask import request


@api.route('/user/<user_id>/subscription', methods=['POST'])
def add_user_subscription(user_id):
    sub = Subscription()
    sub.fromdict(request.json)
    sub.user_id = user_id
    db.session.add(sub)
    db.session.commit()
    return '', 201
