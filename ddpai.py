
from response import (
    FrontCameraInfo,
    RearCameraInfo,
    DDPAIPlayback,
    DDPAIEvent,
    DDPAIParking,
)

from utils import get_value, to_json, to_footage
from client import Client
import api
import socket
from io import BytesIO

class DDPAI:
    def __init__(self, url: str = api.BASE_URL) -> None:
        api.BASE_URL = url
        self.session_token : str = ""
        
    async def is_connected(self, ip: str = api.BASE_URL, port: int = 80, timeout: int = 1) -> bool:
        '''to check connection between host with ddpai dashcam
        
            parameter:
                `ip` : ip address or url string
                `port` : port to check, default = 80
                `timeout` : connnection timeout, default = 1seconds
            
            
            return boolean 
        '''
        if ip.startswith("http"):
            import re
            pattern = r'https?://([\d\.]+)(:\d+)?'
            result = re.search(pattern=pattern, string=ip)
            if not result:
                return False
            
            ip = result.group(1)
        
        try:
            socket.setdefaulttimeout(timeout)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((ip, port))
            
            return True
            
        except Exception as error:
            return False
        
    async def get_session_token(self) -> str:
        '''
        get session id token from dashcam for header request. 
        Not important, you can still communicate with dashcam even without session id token
        '''
        resp = await Client.post(url=api.APIRequestSessionID, header=await self.get_default_header())
        if not resp:
            return None
        
        self.session_token = get_value(resp, key="acSessionId") or ""
        return self.session_token
    
    async def get_mailbox(self) -> list[str]:
        '''
        get mailbox notification string list from dashcam
        '''
        resp = await Client.post(url=api.APIGetMailboxData, header=await self.get_default_header())
        if not resp:
            return None
        
        if get_value(resp, "errcode") in ("0", 0):
            return get_value(resp, 'data')
        
        return None
    
    async def get_camera_info(self, cam: bool = True) -> list[RearCameraInfo] | list[FrontCameraInfo]:
        '''
        get camera information from dashcam.
        
        parameter:
            `True` : for front camera info
            `False`: for rear camera info
            
        return: FrontCameraInfo | RearCameraInfo
        '''
        if cam is True:
            resp = await Client.post(url=api.APIGetBaseInfo, header=await self.get_default_header())
            if not resp:
                return None
            
            return FrontCameraInfo(*resp) if isinstance(resp, dict) else None
        
        else:
            resp = await Client.post(url=api.CAMRearStatus, header=await self.get_default_header())
            if not resp:
                return None
            
            return RearCameraInfo(*resp) if isinstance(resp, dict) else None
            
    async def get_camera_playback(self, cam: bool = True) -> list[DDPAIPlayback]:
        '''
        get camera playback list from dashcam.
        
        parameter:
            `True` : for front camera
            `False`: for rear camera
            
        return: list[DDPAIPlayback]
        '''
        if cam is True:
            url = api.CAMFrontPlayback
        else:
            url = api.CAMRearPlayback
            
        resp = await Client.post(url=url, header=await self.get_default_header())
        if resp is None:
            return None
        
        resp = get_value(resp, "file")
        return [DDPAIPlayback(*r.values()) for r in resp if isinstance(r, dict)]
    
    async def get_camera_event(self, cam: bool = True) -> list[DDPAIEvent]:
        '''
        get camera event list from dashcam.
        
        parameter:
            `True` : for front camera
            `False`: for rear camera
            
        return: list[DDPAIEvent]
        '''
        if cam is True:
            url = api.CAMFrontEvent
        else:
            url = api.CAMRearEvent
            
        resp = await Client.post(url=url, header=await self.get_default_header())
        if resp is None:
            return None
        
        resp = get_value(resp, "event")
        return [DDPAIEvent(*r.values()) for r in resp if isinstance(r, dict)]
    
    async def get_parking_event(self) -> list[DDPAIParking]:
        '''
        get parking event list from dashcam.
        
        return: list[DDPAIParking]
        '''
        resp = await Client.post(url=api.PARKEvent, header=await self.get_default_header())
        if resp is None:
            return None
        
        resp = await get_value(resp=resp, key="event")
        return [DDPAIParking(*r.values()) for r in resp if isinstance(r, dict)]
    
    async def download_file(self, file : DDPAIPlayback | DDPAIEvent) -> BytesIO:
        '''
        download specific file from dashcam.
        
        parameter:
            `file` : DDPAIPlayback | DDPAIEvent 
            
        return: BytesIO
        '''
        file = to_footage(file)
        resp = await Client.download(
            url=api.BASE_URL + file.name, 
            size=file.size,
            header=await self.get_default_header()
        )
        
        return resp
    
    async def set_super_download(self, mode: bool = True) -> str:
        '''
        set super download on or off. when you are downloading a file from dashcam, 
        you might need to turn this one on, then once finished, turn it off back. 
        because thats what happened in ddpai android apps.
        
        parameter: 
            `bool` : True or False
            
        return: response from dashcam
        '''
        return Client.post(
            url= api.APISuperDownload,
            header=await self.get_default_header(),
            body= {
                "switch" : "on" if mode else "off"
            }
        )
    
    async def get_default_header(self) -> dict:
        return {
            "sessionid" : self.session_token,
            "Content-type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; SM-A127F Build/TP1A.220624.014)",
            "Connection": "Close",
            "Accept-Encoding": "gzip"
        }