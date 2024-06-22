#{"user":"admin","password":"admin","level":0,"uid":"22b8d8d2e89ae3bdcom.cam.ddpai_overseas"}

# base url / local ip address
BASE_URL: str = "http://193.168.0.1"


######################### Files endpoint ################################
recordlog: str = F"{BASE_URL}/record.log"
gpxfile: str = F"{BASE_URL}/current.gpx"
gsnfile: str = F"{BASE_URL}/current.gsn"

######################### Settings endpoint ################################
APIGetBaseInfo = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GetBaseInfo"
APIGetMailboxData: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GetMailboxData"
APIRequestSessionID: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_RequestSessionID"
APIQueryUploadLogFileState: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_QueryUploadLogFileState"
APISyncDate: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_SyncDate"
APIGetUpdInfo: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GetUpdInfo"
APIGetCamSimState: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GetCamSimState"
APPAvCamReq: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=APP_AvCamReq"
APPAvCamSet: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=APP_AvCamSet"
APIGeneralSave: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GeneralSave"
APIGeneralQuery: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GeneralQuery"
APIGetCamWifiCapacity: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GetCamWifiCapacity"
APIGetSimTestResult: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GetSimTestResult"

########################### ADAS endpoint ##################################
APIGetAdasStatus: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GetAiAdasDeal"
APISetAdasStatus: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_SetAiAdasDeal"
APICalibrateAdas: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_AdasRecalibration"

########################## Account endpoint ################################
APISetLogonInfo: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_SetLogonInfo"
APIRequestCertificate: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_RequestCertificate"
APIAccountStatus: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_Get_ConnectAccStatus"

######################### PLAYBACK ENDPOINT ################################
APIGetPageFileListStatus: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_Get_PageFileListStatus"
APISuperDownload: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_SuperDownload"
APIGetAlbumState: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GetIntoAlbumState"
# Front Camera endpoint
CAMFrontPlayback: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=APP_PlaybackListReq"
CAMFrontEvent: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=APP_EventListReq"
# Rear Camera endpoint
CAMRearStatus: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GetRearCamConnectInfo"
CAMRearPlayback: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=APP_PlaybackListReq_RearCam"
CAMRearEvent: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=APP_EventListReq_RearCam"
# Parking Event endpoint
PARKEvent: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=APP_ParkingEventListReq"
PARKEventClear: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=APP_ParkingEventListClear"

######################### STREAMING ENDPOINT ################################
RTSPSetCamera: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_SetAppLiveState"
RTSPSwitchCamera: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_PlaybackLiveSwitch"

########################## GPS/GSN ENDPOINT #################################
# GPS Endpoint
GPSStatus: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GetGpsState"
GPSFileList: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GpsFileListReq"
GPSTrackInfo: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_TrackQueryInfo"

GSNFileList: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GsnFileListReq"
GSportFileList: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_SportFileListReq"

GSensorFileList: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GsensorFileListReq"
GSensorRefresh: str = F"{BASE_URL}/vcam/cmd.cgi?cmd=API_GpsGsensorRefresh"
