def to_json(data) :
    import json
    return json.dumps(data, sort_keys=True).encode('utf-8')