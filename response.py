

from dataclasses import dataclass

@dataclass
class FrontCameraInfo:
    nickname: str = ""
    password: str = ""
    ordernum: str = ""
    model: str = ""
    version: str = ""
    mcu_version: int | str = 0
    uuid: str = ""
    sn: str | int = ""
    macaddr: str = ""
    chipsn: str | int = ""
    legalret: int | str = 0
    btnver: int | str = 0
    totalruntime: int | str = 0
    sdcapacity: int | str = 0
    sdspare: int | str = 0
    sdbrand: str = ""
    hbbitrate: int = 0
    hsbitrate: int = 0
    mbbitrate: int = 0
    msbitrate: int = 0
    lbbitrate: int = 0
    lsbitrate: int = 0
    rbbitrate: int = 0
    rsbitrate: int = 0
    default_user: int | str = ""
    is_neeed_update: int | str = 0
    edog_model: str = ""
    edog_version: str | int = ""
    edog_status: int | str = 0
    cid: str = ""
    adas_type: int | str = 0
    stream_type: str | int = 0
    preview_enc_type: int | str = 0
    preview_audio_type: int | str = 0
    preview_mode: int | str = 0
    sensor_cnt: int | str = 0
    rear_picture_in_picture: int | str = 0


@dataclass
class RearCameraInfo:
    default_user: str = ""
    model: str = ""
    nickname: str = ""
    macaddr: str = ""
    version: str | int = 0
    totalruntime: int | str = 0


@dataclass
class DDPAIPlayback:
    index: int = 0
    starttime: int | str = 0
    endtime: int | str = 0
    name: str = ""
    size: int | str = 0


@dataclass
class DDPAIEvent:
    index: int | str = 0
    imgname: str = ""
    bvideoname: str = ""
    bstarttime: str | int = 0
    bendtime: str | int = 0
    bvideosize: str | int = 0


@dataclass
class DDPAIParking:
    type: int | str = 0
    longitude: int | str = 0
    latitude: int | str = 0
    time: int | str = 0
    name: str = ""
    
@dataclass
class CameraFootage:
    index : int = 0
    name: str = ""
    imgname: str = ""
    starttime : int | str = 0
    endtime : int | str = 0
    size : int | str = 0
    
    