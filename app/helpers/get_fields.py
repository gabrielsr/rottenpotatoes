import json
from typing import List


def get_from_json_str(content, *field_keys) -> List[str]:
    """" 
    Get values from a json string
    :param content: json string
    :param field_keys: keys to get from json string
    :return: list of values
    """
    pluck = lambda dict, *args: [dict.get(arg, None) for arg in args]
    adict = json.loads(content)
    return pluck(adict, *field_keys)
