from flask import Flask
from test_app.apis import api as api_blue
from test_app.db import *
from gevent.monkey import patch_all
from test_app import Config

patch_all()
app = Flask(__name__)
app.config.from_object(Config())
db.init_app(app)
with app.app_context():
    print('about to create tables...')
    db.create_all()
    db.session.commit()
    print('done')
app.register_blueprint(api_blue, url_prefix='/api')


@app.route('/')
def hello_world():
    print('root route')
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
