import pkgutil
from flask_sqlalchemy import SQLAlchemy
from dictalchemy.utils import make_class_dictable

db = SQLAlchemy()
make_class_dictable(db.Model)  # makes every model dictable, and thus serializable
# import every class in this package dynamically and automatically, so that tables are created when needed
__path__ = pkgutil.extend_path(__path__, __name__)
for importer, modname, ispkg in pkgutil.walk_packages(path=__path__, prefix=__name__ + '.'):
    __import__(modname)
