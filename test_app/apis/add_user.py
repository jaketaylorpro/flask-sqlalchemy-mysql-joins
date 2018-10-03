from . import api
from ..db import db
from ..db.user import User
from flask import request


@api.route('/user', methods=['POST'])
def add_user():
    user = User()
    user.fromdict(request.json)
    db.session.add(user)
    db.session.commit()
    return '', 201



