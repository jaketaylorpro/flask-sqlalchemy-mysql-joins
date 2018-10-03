import json
import datetime
import decimal


def _json_date_encoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)


def dict_to_json(obj):
    return json.dumps(obj, default=_json_date_encoder)
