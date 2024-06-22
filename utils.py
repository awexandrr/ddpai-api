import json
from response import CameraFootage, DDPAIPlayback, DDPAIEvent

def to_json(resp: str):
    if not isinstance(resp, str):
        return resp
    
    return json.loads(resp)

def to_footage(footage: DDPAIEvent | DDPAIPlayback):
    if isinstance(footage, DDPAIPlayback):
        return CameraFootage(
            index=footage.index,
            name=footage.name,
            starttime=footage.starttime,
            endtime=footage.endtime,
            size=footage.size
        )
    elif isinstance(footage, DDPAIEvent):
        return CameraFootage(
            index=footage.index,
            name=footage.bvideoname,
            imgname=footage.imgname,
            starttime=footage.bstarttime,
            endtime=footage.bendtime,
            size=footage.bvideosize
        )
    else:
        return CameraFootage()
    

def get_value(resp: str | dict | list, key: str):
    if not resp:
        return None

    if isinstance(resp, str):
        try:
            resp = to_json(resp)
            return get_value(resp=resp, key=key)
        except:
            # in case of str is not dict or list, return None
            return None

    if isinstance(resp, list):
        for r in resp:
            retval = get_value(r, key)
            if retval:
                return retval

    if isinstance(resp, dict):
        if key in resp.keys():
            return resp.get(key)

        for k, v in resp.items():
            retval = get_value(v, key)
            if retval:
                return retval

    return None