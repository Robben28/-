from bilibili_api import *
from bilibili_api.user import *
import json, urllib3, time, csv
import bilisearch
bilisearch.get_bestvideo(437643504)
verify = Verify(sessdata="a3c41fe7%2C1608290446%2C45a68*61", csrf="e44cf796e7cb9d90e0b8da41fa2260f5")
my_video = video.VideoInfo(aid=23854706, verify=verify)
#此处输入keyword，l，r
res = bilisearch.get_detail("脚打",1,10)
video_info = my_video.get_video_info()
Mid = video_info['owner']['mid']
user_info = UserInfo(uid=Mid)
uvideo = user_info.get_video()
aa = user_info.get_media_list_content(945437622)
print(json.dumps(video_info, indent=4, ensure_ascii=False))