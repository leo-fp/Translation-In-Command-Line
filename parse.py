#-*-coding:UTF-8-*-
def parse_conf():
    try:
        f = open("./dic_conf.txt")
    except IOError:
        print "ERROR:cannot open dic_conf.txt"
        f.close()
        return
    else:
        list_conf = []      
        string = f.readlines()
        for i in range(2):
            #去除换行符，以":"分割字符串
            item = string[i].strip().split(":")
            list_conf.append(item[1])
        f.close()
        return list_conf

#解析源语种
def parse_from(string_input):
    LIST = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    input_list = list(string_input)
    for each in input_list:
        if each in LIST:
            return "en"
            break;
    #默认中文
    return "zh"
