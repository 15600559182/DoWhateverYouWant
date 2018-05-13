import time
import itchat

@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:
        # 发送一条提示给文件助手
        itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
                        (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
                         msg['User']['NickName'],
                         msg['Text']), 'filehelper')
        # 回复给好友
        return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Text'])


if __name__=="__main__":

    #登录
    itchat.auto_login(hotReload=True)
    # name = itchat.search_friends(name=u'--')
    # codeName = name[0]["UserName"]
    # print(codeName)
    # #发送消息 你好！我是小文机器人，基于python的itchar框架开发。以后我会骚扰经常你的,请多指教！
    # itchat.send(
    #     '#号后边是注释 更短了'
    #     , toUserName=codeName)
    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()


    #@itchat.msg_register(itchat.content.TEXT)
    #def print_content(msg):
    #    print(msg['Text'])


    #itchat.auto_login()
   # itchat.run()

    # 获取好友列表
    # friends = itchat.get_friends(update=True)[0:]
    #
    # # 初始化计数器，有男有女，当然，有些人是不填的
    # male = female = other = 0

    # 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
    # 1表示男性，2女性
    # for i in friends[1:]:
    #     sex = i["Sex"]
    #     if sex == 1:
    #         male += 1
    #     elif sex == 2:
    #         female += 1
    #     else:
    #         other += 1
    #
    # # 总数算上，好计算比例啊～
    # total = len(friends[1:])
    #
    # # 好了，打印结果
    # print    (u"男性好友：%.2f%%" % (float(male) / total * 100))
    # print    (u"女性好友：%.2f%%" % (float(female) / total * 100))
    # print    (u"其他：%.2f%%" % (float(other) / total * 100))

    # 获取好友列表
    # friends = itchat.get_friends(update=True)[0:]
    # for i in friends:
    #     # 获取个性签名
    #     signature = i["Signature"]
    # print(signature)
    # for i in friends:
    #     # 获取个性签名
    #     signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
    #     # 正则匹配过滤掉emoji表情，例如emoji1f3c3等
    #     rep = re.compile("1f\d.+")
    #     signature = rep.sub("", signature)
    #     print(signature)







    print("机器人结束")


