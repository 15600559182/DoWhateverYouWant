# -*- coding utf-8 -*-

import itchat


"""
 微信工具类
    
"""
class WeiXinUtil1:
    itchat.auto_login(hotReload=True)

    """
    初始化方法
        登录微信用户账号
        
        if:检测不可用本地登录
            生成二维码
            二维码发送到邮箱
        else:可本地登录
            登录即可
            
    """
    def __init__(self):
        print (1)

    def print1(self):

        print ("1")


if __name__ == "__main__":
    itchat.auto_login(hotReload=True)

    print (1)


