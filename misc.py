def none_to_empty_string(value):
    return value if value else ''


from datetime import datetime, timedelta
from requests.structures import CaseInsensitiveDict


def json_serialize_datetime(obj):
    """
    Example Usage:
    j = json.dumps(d, default=json_serialize_datetime)
    """
    # to convert back use: iso8601.parse_date()
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, CaseInsensitiveDict):  # a dict implementation used by the Requests library for storing headers
        return dict(obj)
    else:
        raise TypeError("Unserializable object %s of type %s" % (obj, type(obj)))


import time
import os


def file_mtime_older_than(path, days=0):
    return (time.time() - os.path.getmtime(path)) > timedelta(days=days).total_seconds()
