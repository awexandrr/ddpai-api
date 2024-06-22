
import asyncio
from ddpai import DDPAI

async def main():
    client = DDPAI()
    if not await client.is_connected():               # check if dashcam is connected or not
        return
    
    await client.get_session_token()                  # get session id token
    print(await client.get_mailbox())                 # get mailbox notification
    print(await client.get_camera_info(True))         # get front camera info
    print(await client.get_camera_info(False))        # get rear camera info
    print(await client.get_camera_playback(True))     # get front camera playback 
    print(await client.get_camera_playback(False))    # get rear camera playback 
    
    print(await client.get_parking_event())           # get parking event 
    print(await client.get_camera_event(True))        # get front camera event playback details
    print(await client.get_camera_event(False))       # get rear camera event playback details

    # download video playback from dashcam
    playback = await client.get_camera_playback()     # get playback list
    await client.set_super_download(True)             # turn on super download mode
    for video in playback:
        mp4 = client.download_file(video)              # start downloading the file
        with open(video.name, "wb") as vidfile:  
            vidfile.write(mp4)                        # save downloaded file
        
    await client.set_super_download(False)            # turn off super download mode
    
    
if __name__ == '__main__':
    asyncio.run(main())