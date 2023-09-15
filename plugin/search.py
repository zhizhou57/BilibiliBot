import json

from config.config import Config
import requests
headers = Config.headers


def search_user(username: str) -> dict:
    url = "https://api.bilibili.com/x/web-interface/search/all/v2"
    search_url = url + "?keyword=" + username
    response = requests.get(search_url, headers=headers)
    if response.content:
        response_dic = json.loads(response.content)
        if response_dic:
            data = response_dic.get('data')
            if data and response_dic.get('code') == 0:
                result = data.get('result')
                if isinstance(result, list) and len(data) > 0:
                    user_result = None
                    for result_dic in result:
                        result_type = result_dic.get('result_type')
                        if result_type == 'bili_user':
                            user_result = result_dic.get('data')
                    if isinstance(user_result, list) and len(user_result) > 0:
                        for user_dict in user_result:
                            assert user_dict.get('type') == 'bili_user'
                            uname = user_dict.get('uname')
                            mid = user_dict.get('mid')
                            usign = user_dict.get('usign')
                            print("搜索到第一个用户 ", uname, "mid:", mid, "个性签名: " + usign)
                            return {'uname':uname, 'mid':mid, 'usign':usign}
                    else:
                        print("搜索结果无用户")
                else:
                    print("搜索无结果")


def fetch_user_followings(user_info: dict, pn: int = 1, order_type: bool = False) -> tuple:
    '''
    获取用户关注
    :param user_info: 用户信息，包含mid
    :param order_type: 排列顺序，为True表示关注顺序，为False表示最常访问顺序
    :return: 关注信息
    '''
    url = "https://api.bilibili.com/x/relation/followings"
    vmid = user_info.get("mid")
    if vmid:
        url += "?vmid=" + str(vmid)
        if order_type:
            url += "?order_type=" + "attention"
        if pn > 1:
            url += "?pn=" + str(pn)
        response = requests.get(url, headers=headers)
        following = json.loads(response.content)
        data = following.get('data')
        if following.get('code') == 0 and data:
            following_list = data.get('list')
            total_num = data.get('total')
            if isinstance(following_list, list) and len(following_list) > 0:
                return following_list, total_num
            else:
                print("用户" + user_info.get('uname'), "无关注")
    else:
        print("无用户mid无法获取关注")
    return list(), 0

def build_analysis_info(following_list: list, user_info: dict) -> str:
    '''
    根据关注信息构建用于分析的信息
    :param following_info: 关注信息列表
    :return:
    '''
    if len(following_list) > 0:
        uname = user_info.get('uname')
        sign = user_info.get('usign')
        desc = "我在视频网站Bilibili上的名字叫做" + uname + ", 我的个性签名为：" + sign + "\n"
        desc += "以及下面是我在视频网站Bilibili上的关注信息，请你根据这些分析猜测下我从事什么样的职业或者在哪上学？以及有什么兴趣爱好？下面是我的关注及其签名的信息：\n"
        for following in following_list:
            uname = following.get('uname').strip()
            sign = following.get('sign').strip()
            official_verify = following.get('official_verify')
            if official_verify:
                is_official_verify = official_verify.get('type')
                official_verify_info = official_verify.get('desc')
                if is_official_verify == -1:
                    continue
            following_desc = "up主：{}, 该up主个性签名为：{}\n".format(uname, sign)
            desc += following_desc
        return desc

def search_user_by_following(mid: str, username: str)-> dict:
    user_info = {'username': "zhi舟", "mid": mid, "usign": ""}
    following_list, total_num = fetch_user_followings(user_info)
    for following in following_list:
        uname = following.get('uname')
        if uname == username:
            mid = following.get('mid')
            usign = following.get('sign')
            return {'uname':uname, 'mid':mid, 'usign':usign}


username = "CircularArc"
user_info = search_user(username)
if not user_info:
    print("未搜索到该用户, 从关注列表查询该用户")
    mid = "252162735"
    user_info = search_user_by_following(mid, username)
    if not user_info:
        print("仍未搜索到该用户，请检查用户名")
        exit(-1)
following_list, total_num = fetch_user_followings(user_info)
if following_list:
    analysis_info = build_analysis_info(following_list, user_info)
    print(analysis_info)
else:
    print("该用户无关注或关注不可见")
