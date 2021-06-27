import tkinter as tk
import tkinter.messagebox
import bilisearch
import bilitrack
import time
window = tk.Tk()
window.title('哔哩哔哩小助手 Bilibili Assistant Ver:1.2')
window.geometry('500x350')
#窗口图标ico（绝对路径）
#welcome
print("Welcome to use Bilibili Assistant!")
print("Select any function to execute!")
print("请选择要执行的功能...")
#About信息
def about():
    tkinter.messagebox.showinfo(title='About', message='[Main Code]A magic Bang&33\n[Credits]Thanks to Passkou for Bilibili_Api\nRunning on Python 3')  
#功能函数
def submit():
    keyword = inpt.get()
    inin = keyword.split(',')
    keyword = inin[0]
    startpage = int(inin[1])
    endpage = int(inin[2])
    print("正在查询...请稍后")
    print("查询关键字",keyword,"从",startpage,"页","至",endpage,"页")
    total,page = bilisearch.search(keyword[0])
    resstr = "共查询到"+str(total)+"条相关信息，共计"+str(page)+"页"
    res.config(text='查询结果：'+resstr)
    tt = bilisearch.get_detail(keyword,startpage,endpage)
    for x in tt:
        resx = 'AV：'+str(x['aid'])+',作品名称：'+x['title']+'\n播放量：'+str(x['play'])+',UP主：'+x['author']+'   '+str(x['mid'])+'    粉丝数：'+str(bilisearch.get_fannum(x['mid']))
        showres.insert('insert',resx+'\n')
def starttrack():
    inin = trackin.get()
    author = inin.split(',')
    trafeed.insert('insert','请点击开始监控来监控以下up主粉丝变化，请保持程序运行，监控时期会出现gui卡死情况，请一段时间后打开res.csv查看结果：\n')
    print("UID:",inin)
    for x in author:
        trafeed.insert('insert',x+'\n')
        video = bilisearch.get_bestvideo(int(x))
        trafeed.insert('insert','当前粉丝数：'+str(bilisearch.get_fannum(int(x)))+'\n')
        trafeed.insert('insert','UP的最多播放视频为：'+video['title']+'\n')
        trafeed.insert('insert','当前播放量：'+str(video['play'])+'\n')
        #print("UP主:")
def track():
    inin = trackin.get()
    author = inin.split(',')
    bilitrack.start(author)  #监控函数，csv写入 死循环
def uidsearchstart():
    keyword = uidsearch.get()
    res = bilisearch.get_uid(keyword)
    lenn = len (res)
    i = 0
    def ins(i):
        if i >= lenn:
            return
        else :
            uidres.insert('insert','搜索到用户名:'+res[i]['uname']+'   Ta的Uid为:'+str(res[i]['mid'])+'\n')
            uidres.after(10,ins,i+1)
    if lenn == 0:
        uidres.insert('insert','无结果!\n')
    else:
        ins(1)
def getvideoinfo():
    bvid = inbvid.get()
    info = bilisearch.get_videodetail(bvid)
    infores.insert('insert','AV:'+str(info['aid'])+'\n')
    infores.insert('insert','分类:'+info['tname']+'\n')
    if info['copyright'] == 1:
        cp = '是'
    else :
        cp = '否'
    infores.insert('insert','是否原创:'+cp+'\n')
    infores.insert('insert','标题:'+info['title']+'\n')
    infores.insert('insert','描述:'+info['desc']+'\n')
    infores.insert('insert','发布时间:'+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info['pubdate']))+'\n')
    infores.insert('insert','播放:'+str(info['stat']['view'])+'\n')
    infores.insert('insert','弹幕:'+str(info['stat']['danmaku'])+'\n')
    infores.insert('insert','点赞:'+str(info['stat']['like'])+'\n')
    infores.insert('insert','投币:'+str(info['stat']['coin'])+'\n')
    infores.insert('insert','分享:'+str(info['stat']['share'])+'\n')
    infores.insert('insert','评论:'+str(info['stat']['reply'])+'\n')
    infores.insert('insert','标签:'+str(info['dynamic'])+'\n')
def get_bvid():
    aid = inaid.get()
    bvid = bilisearch.get_bvid(aid)
    bvidres.insert('insert',bvid)
def get_biliuser():
    mid = inmid.get()
    info,live,videos = bilisearch.get_biliuser(mid)  #获取相关信息
    userres.insert('insert','用户名:'+str(info['name'])+"   签名:"+str(info['sign'])+'   性别:'+info['sex']+'\n')  
    userres.insert('insert','关注:'+str(info['following'])+'   粉丝:'+str(info['follower'])+'\n')#打印基本信息
    if live['liveStatus'] == 1:
        livestatus = '是'
    else :
        livestatus = '否'  #打印直播信息
    userres.insert('insert','直播间链接:'+live['url']+"   直播标题:"+live['title']+'    是否开播中:'+livestatus+'   当前观众:'+str(live['online'])+'\n')
    playnum=0
    for x in videos:
        userres.insert('insert','投稿名称:'+x['title']+'    bv:'+x['bvid']+'    播放数:'+str(x['play'])+'\n')
        playnum=playnum+x['play']
        userres.insert('insert','时长:'+x['length']+'    发布时间:'+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(x['created']))+'\n')
    print("用户:",info["name"],"粉丝:",info['follower'],"关注:",info['following'],"总播放量:",playnum)
    print("长期综合热度:",float(info['follower'])/float(playnum)*22.33*1000)

#关键词查找
resstr = ''
text1 = tk.Label(window,text='请输入关键词以及查询到X页至X页\n页数用逗号(英文格式)分开\n例:小鸟伏特加,1,3')
bt = tk.Button(window,text='查找',command=submit,relief='groove')
res = tk.Label(window,text='查询结果：'+resstr)
showres = tk.Text(window,relief='solid')
inpt = tk.Entry(window,relief='solid')
#粉丝数量监控
res.config(text='查询结果：'+resstr)
btt = tk.Button(window,text='查询',command=starttrack,relief='groove')
sttrack = tk.Button(window,text='开始监控',command=track,relief='groove')
trafeed = tk.Text(window,relief='solid')
trackin = tk.Entry(window,relief='solid')
tracktext = tk.Label(window,text='请以逗号为间隔输入要监控的up主uid')
#用户名查uid
uidsearch = tk.Entry(window,relief='solid')
uidres = tk.Text(window,relief='solid')
uidbt = tk.Button(window,text='查找Up主',command=uidsearchstart,relief='groove')
#视频详细信息
inbvid= tk.Entry(window,relief='solid')
inbvidbt = tk.Button(window,text='获取信息',command=getvideoinfo,relief='groove')
infores = tk.Text(window,relief='solid')
#bvid
inaid = tk.Entry(window,relief='solid')
inaidbt = tk.Button(window,text='查询BVid',command=get_bvid,relief='groove')
bvidres = tk.Text(window,relief='solid')
#uid查up详细信息
inmid = tk.Entry(window,relief='solid')
inmidbt = tk.Button(window,text='查询用户信息',command=get_biliuser,relief='groove')
userres = tk.Text(window,relief='solid')
#切换菜单
def videoinfo():
    #隐藏界面
    trackin.pack_forget()
    tracktext.pack_forget()
    sttrack.pack_forget()
    btt.pack_forget()
    trafeed.pack_forget()
    sttrack.pack_forget()
    uidsearch.pack_forget()
    uidres.pack_forget()
    uidbt.pack_forget()
    inaid.pack_forget()
    inaidbt.pack_forget()
    bvidres.pack_forget()
    inbvidbt.pack_forget()
    infores.pack_forget()
    inbvid.pack_forget()
    inmid.pack_forget()
    inmidbt.pack_forget()
    userres.pack_forget()
    #显示界面
    text1.pack()
    inpt.pack()
    bt.pack()
    res.pack()
    showres.pack()
    print("[Console]当前功能已切换至-->关键字搜索相关视频")
    print("[Console]请按格式正确输入关键字来查找相关视频")
def upinfo():
    #隐藏界面
    inpt.pack_forget()
    bt.pack_forget()
    res.pack_forget()
    showres.pack_forget()
    text1.pack_forget()
    uidsearch.pack_forget()
    uidres.pack_forget()
    uidbt.pack_forget()
    inaid.pack_forget()
    inaidbt.pack_forget()
    bvidres.pack_forget()
    inbvidbt.pack_forget()
    infores.pack_forget()
    inbvid.pack_forget()
    inmid.pack_forget()
    inmidbt.pack_forget()
    userres.pack_forget()
    #显示界面
    trackin.pack()
    tracktext.pack()
    sttrack.pack()
    btt.pack()
    trafeed.pack()
    sttrack.pack()
    print("[Console]当前功能已切换至-->UP主粉丝数量监控")
    print("[Console]循环间隔当前已设置为300秒/次")
def uidsearch1():
    #隐藏界面
    inpt.pack_forget()
    bt.pack_forget()
    res.pack_forget()
    showres.pack_forget()
    text1.pack_forget()
    trackin.pack_forget()
    tracktext.pack_forget()
    sttrack.pack_forget()
    btt.pack_forget()
    trafeed.pack_forget()
    sttrack.pack_forget()
    inaid.pack_forget()
    inaidbt.pack_forget()
    bvidres.pack_forget()
    inbvidbt.pack_forget()
    infores.pack_forget()
    inbvid.pack_forget()
    inmid.pack_forget()
    inmidbt.pack_forget()
    userres.pack_forget()
    #显示界面
    uidsearch.pack()
    uidbt.pack()
    uidres.pack()
    print("[Console]当前功能已切换至-->用户名查找UID")
    print("[Console]等待输入用户名...")
def bvid1():
    inpt.pack_forget()
    bt.pack_forget()
    res.pack_forget()
    showres.pack_forget()
    text1.pack_forget()
    trackin.pack_forget()
    tracktext.pack_forget()
    sttrack.pack_forget()
    btt.pack_forget()
    trafeed.pack_forget()
    sttrack.pack_forget()
    uidsearch.pack_forget()
    uidbt.pack_forget()
    uidres.pack_forget()
    inbvidbt.pack_forget()
    infores.pack_forget()
    inbvid.pack_forget()
    inmid.pack_forget()
    inmidbt.pack_forget()
    userres.pack_forget()
    inaid.pack()
    inaidbt.pack()
    bvidres.pack()
    print("[Console]当前功能已切换至-->AV号BV号转换")
def videoinfo1():
    inpt.pack_forget()
    bt.pack_forget()
    res.pack_forget()
    showres.pack_forget()
    text1.pack_forget()
    trackin.pack_forget()
    tracktext.pack_forget()
    sttrack.pack_forget()
    btt.pack_forget()
    trafeed.pack_forget()
    sttrack.pack_forget()
    uidsearch.pack_forget()
    uidbt.pack_forget()
    uidres.pack_forget()
    inaid.pack_forget()
    inaidbt.pack_forget()
    bvidres.pack_forget()
    inmid.pack_forget()
    inmidbt.pack_forget()
    userres.pack_forget()
    inbvid.pack()
    inbvidbt.pack()
    infores.pack()
    print("[Console]当前功能已切换至-->视频详细信息查询")
    print("[Console]请输入正确的BV号或进行AV号转换")
def userinfo1():
    inpt.pack_forget()
    bt.pack_forget()
    res.pack_forget()
    showres.pack_forget()
    text1.pack_forget()
    trackin.pack_forget()
    tracktext.pack_forget()
    sttrack.pack_forget()
    btt.pack_forget()
    trafeed.pack_forget()
    sttrack.pack_forget()
    uidsearch.pack_forget()
    uidbt.pack_forget()
    uidres.pack_forget()
    inaid.pack_forget()
    inaidbt.pack_forget()
    bvidres.pack_forget()
    inbvid.pack_forget()
    inbvidbt.pack_forget()
    infores.pack_forget()
    inmid.pack()
    inmidbt.pack()
    userres.pack()
    print("[Console]当前功能已切换至-->用户详细信息查询")
    print("[Console]请输入用户UID...")
# 创建菜单
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
# 装入容器
menubar.add_cascade(label='Menu', menu=filemenu)
filemenu.add_command(label='关键字搜索相关视频', command=videoinfo)
filemenu.add_command(label='AV号转BV号', command=bvid1)
filemenu.add_command(label='用户名查找UID', command=uidsearch1)
filemenu.add_command(label='UP主粉丝数量监控', command=upinfo)
filemenu.add_command(label='视频详细信息查询', command=videoinfo1)
filemenu.add_command(label='用户详细信息查询', command=userinfo1)

#filemenu.add_command(label='Adding', command=do_job)
filemenu.add_separator()    # 添加一条分隔线
#filemenu.add_command(label='Fuck u', command=do_job)
menubar.add_cascade(label='About', command=about)
#welcome.pack()
window.config(menu=menubar)
window.mainloop()



