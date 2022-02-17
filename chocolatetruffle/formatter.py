import json


def _serialize_sets(obj):
    """Convert sets to lists when dumping json data"""
    if isinstance(obj, set) :
        try :
            result = sorted(list(obj))
        except TypeError :
            # Cannot be sorted
            result = list(obj)
        finally :
            return result
    return obj


def to_json(obj, indent=4, out: str=None, encoding='utf8') :
    """Convert python built-in data types to json"""
    dump_str = json.dumps(obj, indent=indent, default=_serialize_sets)
    if out is None :
        return dump_str
    else :
        with open(out, 'w', encoding=encoding) as f :
            f.write(dump_str)
        return None


def jprint(obj, indent=4) :
    """Pretty print a json data"""
    print(to_json(obj, indent=indent))
