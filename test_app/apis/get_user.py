from . import api
from ..db.user import User


@api.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    print('loading user: ' + str(user_id))
    user = User.query.filter_by(id=user_id).first()
    return user.to_json()
