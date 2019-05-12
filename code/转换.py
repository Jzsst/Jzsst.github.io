# 开发者：Jzsst
# 最近更新时间：2019-04-24
# 免费
def add_center():
    flag = 0
    print("请注意路径格式,文件格式为txt。例：C:/Users/user/Desktop/test.txt")
    print("输入需要修改文件的地址:",end='')
    str_file_old_path=input()
    #处理文件名
    str_s= str_file_old_path.split("/")
    new_file =str_s[len(str_s)-1].split(".")
    # 防止老文件影响
    new_f = open(new_file[0] + "_center." + new_file[1], "w")
    new_f.close()
    #写入
    new_f=open(new_file[0]+"_center."+new_file[1],"a",encoding='utf-8')
    for line in open(str_file_old_path,"r",encoding='utf-8'):  # utf-8  or  gbk  自己改
        # 判断哪些需要添加
        if (len(line.strip()) > 0 and line[0] != '!' and flag == 2):
            #处理一行文本
            new_f.write("<p align=\"center\">"+line.strip()+"</p>")
        else :
            new_f.write(line)
        # 解决blog开始解释部分
        if(line.strip() == "---" and (flag == 0 or flag == 1)):
            flag = flag + 1
    new_f.close()
    print("完成")

if __name__ == '__main__':
    add_center()