import json
import hashlib
def to_json(data) :
    return json.dumps(data, sort_keys=True).encode('utf-8')

def to_sha256(data) :
    return hashlib.sha256(data).hexdigest()