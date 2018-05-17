# -*- coding utf-8 -*-

import itchat
import datetime

"""
 微信工具类
    
"""
class WeiXinUtil1:
    """
    初始化方法
        登录微信用户账号
    """
    def __init__(self):
        itchat.auto_login(enableCmdQR=True)
        print(1)

    def print1(self):

        print("1")


if __name__ == "__main__":
    WeiXinUtil1()
    now = datetime.datetime.now()
    print(now)
    print (1)


