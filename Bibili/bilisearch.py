from bilibili_api import *
from bilibili_api.user import *
import json, urllib3, time
from bilibili_api.video import *
http = urllib3.PoolManager()
searchapi = 'https://api.bilibili.com/x/web-interface/search/type?'
def search(keyword):#输入关键词,返回相关结果的数量
    searchlist = http.request("GET",searchapi+'&keyword='+keyword+'&search_type=video')
    search_info = json.loads(searchlist.data.decode())
    searchres = []
    author = set()
    return search_info["data"]["numResults"],search_info["data"]["numPages"]
def get_detail(keyword,pagestart,pageend):#输入关键词，返回范围内视频的详细信息
    number,pagenumber = search(keyword)
    searchres = []
    if pagestart > pagenumber:
        return searchres
    if pageend > pagenumber: 
        pageend = pagenumber
    for x in range (pagestart,pageend+1):
        tmp = http.request("GET",searchapi+'&page='+str(x)+'&'+'keyword='+keyword+'&search_type=video')
        onepage = json.loads(tmp.data.decode())['data']['result']
        for x in onepage:
            if keyword in x['title']: #or keyword in x['author']:只收集题目中包含关键词的
                x['title'] = x['title'].replace('<em class="keyword">','')
                x['title'] = x['title'].replace('</em>','')
                searchres.append(x)
    return searchres
def get_fannum(mid):#获取视频信息
    user_info = UserInfo(uid=mid)
    info = user_info.get_info()
    return info['follower']
def get_bestvideo(mid):#获取Up最高播放视频
    user_info = UserInfo(uid=mid)
    info = user_info.get_video()
    ans = info[0]
    for x in info:
        if x['play'] > ans['play']:
            ans = x
    return ans
def get_uid(keyword):
    searchlist = http.request("GET",searchapi+'&keyword='+keyword+'&search_type=bili_user')
    search_info = json.loads(searchlist.data.decode())
    try :
        res = search_info['data']['result']
    except:
        res = []
        print("查找不到相关用户!")
    return res



def get_videodetail(id):
    video_info = VideoInfo(bvid=id)
    info = video_info.get_video_info()
    return info

def get_bvid(id):
    try:
        video_info = VideoInfo(aid=int(id))
        info = video_info.get_video_info(is_simple=True)
        return info['bvid']
    except:
        print("输入Av号无效或视频不存在")
        return 'Av不存在'
def get_biliuser(mid):
    user_info = UserInfo(uid=mid)
    info = user_info.get_info()
    live = user_info.get_live_info()
    videos = user_info.get_video()
    return info,live,videos

    