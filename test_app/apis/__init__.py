import pkgutil

from flask import Blueprint

api = Blueprint('api', __name__)

# import every class in this package dynamically and automatically, so that api routes are created when needed
__path__ = pkgutil.extend_path(__path__, __name__)
for importer, modname, ispkg in pkgutil.walk_packages(path=__path__, prefix=__name__ + '.'):
    __import__(modname)
