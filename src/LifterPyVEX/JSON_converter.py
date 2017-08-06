import json

def to_JSON(ty, sty, args):
    target = {'Type' : ty, 'SubType' : sty, 'Args' : args}
    return json.dumps(target)
