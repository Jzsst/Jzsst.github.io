# 开发者：Jzsst
# 最近更新时间：2019-04-24
# 免费
def add_center():
    flag = 0
    for line in open("C:/Users/Jzsst/Desktop/test.txt","r",encoding='utf-8'):  # 返回一个文件对象
        # 判断哪些需要添加
        if (len(line.strip()) > 0 and line[0] != '!' and flag == 2):
            #处理一行文本
            print("<p align=\"center\">"+line.strip()+"</p>")
        else :
            print(line)
        # 解决blog开始解释部分
        if(line.strip() == "\---" and (flag == 0 or flag == 1)):
            flag = flag + 1

if __name__ == '__main__':
    add_center()