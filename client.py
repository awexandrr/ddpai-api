

'''
Client module to communicate with ddpai dashcam
'''

import aiohttp
from io import BytesIO

class Client:
    timeout = 10
    @staticmethod
    async def get(self, url : str, header : dict = {}) -> str:
        async with aiohttp.ClientSession(timeout = aiohttp.ClientTimeout(Client.timeout)) as session:
            async with session.get(url, header=header) as resp:
                if resp.status != 200:
                    return None
                
                return await resp.json()
    
    @staticmethod    
    async def post(self, url : str, header : dict = {}, body : dict = {}) -> str:
        async with aiohttp.ClientSession(timeout = aiohttp.ClientTimeout(Client.timeout)) as session:
            async with session.post(url, json = body, header=header) as resp:
                if resp.status != 200:
                    return None
                
                return await resp.json()

    @staticmethod
    async def download(self, url : str, size: int, header : dict = {}) -> BytesIO:
        """
        `url` str : url to file
        `name` str : filename to download
        `size` int : size of the file to download in bytes
        """
        
        dlbytes = bytes()
        timeout = Client.timeout * 30 
        async with aiohttp.ClientSession(timeout = aiohttp.ClientTimeout(timeout)) as session:
            async with session.get(url, header=header) as resp:
                if resp.status != 200:
                    return None
                
                async for chunk in resp.content.iter_chunked(size):
                    dlbytes += (chunk)
  
        return BytesIO(dlbytes)