# /usr/bin/env python
"这是一个将用户输入数据写入到文件的类"

import os

class makeTextFile(object):
    def makeAndWirte(self, fname):
        ls = os.linesep
        while True:
            if os.path.exists(fname):   #查找是否有这个文件 有则返回True
                print("Error: '%s' already exists" % fname)
                print("请输入新的路径")
                fname = input()
            else:
                break

        all = []

        print("\nEnter lines ('.' by iteself to quit).\n")

        while True:
            entry = input()
            if entry == '.':
                break
            else:
                all.append(entry)

        fobj = open(fname, 'w')
        "遍历的方式逐行写到文件中"
        fobj.writelines(['%s%s' % (x, ls) for x in all])
        fobj.close()
        print("DONE!")


if __name__ == '__main__':
    print("请开始你的表演")
    filePath = "D:\python\demo1.txt"
    m = makeTextFile()
    m.makeAndWirte(filePath)
