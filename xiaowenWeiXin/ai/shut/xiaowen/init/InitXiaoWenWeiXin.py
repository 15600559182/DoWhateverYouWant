# -*- coding utf-8 -*-

from xiaowenWeiXin.ai.shut.xiaowen.weixinUtil.WeiXinUtil import WeiXinUtil1

"""
初始化小文AI微信类
"""
class InitXiaoWenWeiXin:

    """
    初始化项目方法
    """
    def __init__(self):

        # 登录微信账户
        WeiXinUtil1()

        # 开启自动发Job
        print("开启Job")


if __name__ == "__main__":
    InitXiaoWenWeiXin()
    print('end')

