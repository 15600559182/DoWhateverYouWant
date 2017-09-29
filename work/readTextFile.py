#!/usr/bin/env python

class readTextFile(object):
    def readTextByFilePath(self, filePath):
        # 读取文件并输出内容
        try:
            f = open(filePath, "r")
        except IOError as e:
            print(e)
        else:
            for rowText in f:
                print(rowText, end=' ')
            f.close()

if __name__ == '__main__':
    r = readTextFile()
    r.readTextByFilePath("D:\python\demo1.txt")