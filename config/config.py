#在这里配置你的机器人操作类中需要的东西，图方便就不写JSON了，大家这样也好理解
class Config:

    # 机器人发信headers
    headers = {
    "referer": "https://message.bilibili.com/",
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'cookie' : "buvid3=18A79241-19D4-44AF-A5C9-316CEA53034E80650infoc; i-wanna-go-back=-1; _uuid=55C1AE3E-922A-F464-6912-8EEA8C68A6FC81169infoc; FEED_LIVE_VERSION=V8; DedeUserID=252162735; DedeUserID__ckMd5=dd5a30de56f99304; hit-dyn-v2=1; rpdid=0zbfAGq210|ssLZdJkg|39a|3w1QdqdI; header_theme_version=CLOSE; hit-new-style-dyn=1; buvid_fp_plain=undefined; LIVE_BUVID=AUTO3016891742468043; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; b_ut=5; b_nut=1693296368; buvid4=269CCCE2-4021-9EB8-9BB8-E0C129A3645781969-023062521-XGlrq6aGdcQnnjBBQv3JuA56WadI04JOigybUA3wvC3a1c6AdzDlCA%3D%3D; SESSDATA=8ed8a196%2C1710063240%2C68b7d%2A91CjArkBvy7NM2XkiABAML2j5ZwCOsha2ATyFO1i6XMouZLp58EzP3vGDZRp7tqj7Os9ASVjVuVXRlaVRSVFFxbEJOYTFQYkRYRUM5MTcxaHpfcUR5Q1FwRXRmOWQ1NzBSS2xzX2NoUXN2MmJlbm9FUTRlc3JtWWJ5UnFHbkx6Tkw0bTBXYXBjbURBIIEC; bili_jct=7d49ace850cf4d9e31c87b80a8ba219f; sid=8et4xdj0; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ3NzA0NDMsImlhdCI6MTY5NDUxMTI0MywicGx0IjotMX0.fPbWLSkPyCGTRtakctuecY3VnbH8Q5UeKs4_LSU3HNo; bili_ticket_expires=1694770443; bsource=search_google; CURRENT_QUALITY=116; b_lsid=D2A106AD7_18A9694EDBF; bp_video_offset_252162735=841404726338650372; innersign=0; fingerprint=410414b060bffafcdc233c4c512e2536; home_feed_column=4; browser_resolution=466-918; PVID=3; buvid_fp=410414b060bffafcdc233c4c512e2536"
    }
    # B站账号鉴权 -> cookie 的 bili_jct
    csrf_token = '7d49ace850cf4d9e31c87b80a8ba219f'

    # 机器人UID
    robot_uid = 252162735

    # TODO 消息刷新心跳 -> 秒数 建议 在 2 ~ 3 之内 如果设置为 1 代表每位用户1秒内最多可以发送1条消息，可以同时发送 根据需求加快心跳 太低可能会给B站造成负担，请不要低于2
    heartbeat_interval = 3

    # python词库的使用与否 如果要用webhook去当词库，那么建议不使用python词库 以免重复推送
    pythonDicState = True

    '''
    webhook配置区域
    在这里设置外部接口，如果你有兴趣可以使用返回值来实现外部通信同样的功能
    比如，webhook向挂钩地址请求后，受请求的一方处理这个值，然后直接返回，返回后python把消息推送给机器人
    你也可以搭配下面的Socke，webhook收消息，Socke发消息
    '''
    # webhook挂钩状态 False则不进行发送
    webHookState = False

    webHookDicState = False

    # webhook挂钩地址 可设为多个，不要太多 即使我已经使用了线程操作
    webHookUrl = [
        'https://api.misakaloli.com/api/misaka/WebHook.php'
    ]

    '''
    Socke配置区域 目前采用的是UDP
    这里是我专门留出的，外部可以直接向这个地址去发送请求，收到后直接推送给机器人
    '''
    # Socke通信状态 False则不启动服务端
    SocketState = False



    #----------直播机器人设置-----------

    #直播间机器人状态
    liveDicState = False

    #直播消息心跳时间，同上
    live_heartbeat_interval = 3

    #轮询直播间
    live_id = 312381




