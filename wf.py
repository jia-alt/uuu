import sys
import getopt
import re
import os

def count_split(str):
    text= re.findall(r'[a-z0-9^-]+', str)              #指定特殊字符
             #字符替换
    dict = {}                                    #创建字典
    for str in text:                             #遍历文件内单词
        if str in dict.keys():
           dict[str] = dict[str] + 1
        else:
           dict[str] = 1
    word_list=sorted(dict.items(), key=lambda x: x[1], reverse=True)
    return word_list


def file_read(filename):  # 打开文件
    f = open(filename, 'r', -1, 'utf-8')
    text = f.read().lower()
    word_list = count_split(text)
    f.close()
    return word_list
def get_words(argv):             # 根据输入的命令行参数执行对应操作
    if len(argv) == 2:                 # 功能1
        try:
            list = file_read(argv[-1])
            opts, args = getopt.getopt(argv, "sh", ["ifile", "ofile"])
        except getopt.GetoptError:
            print("test.py -i <inputfile> -o <outputfile>")
            sys.exit(2)
        for opt, arg in opts:
            if opt == "-s":
                num = len(list)
                print('total',num)
                print('\n')
                for word in list:
                    print('{:20s}{:>5d}'.format(word[0], word[1]))
    elif len(argv) == 1:                #功能2.3
        file = argv[-1] + '.txt'
        is_file = os.path.exists(file)
        if is_file:
            list = file_read(file)
            if len(list) <=10:
                print('total', len(list), 'words')
                print('\n')
                for item in list:
                    print('{:20s}{:>5d}'.format(item[0], item[1]))
            else:                       # 多于10条
                print('total', len(list), 'words')
                print('\n')
                for i in range(10):
                    print('{:20s}{:>5d}'.format(list[i][0], list[i][1]))

        else:
            if argv[-1] != '-s':
                folder_name = argv[-1]
                os.chdir(folder_name)
                filename_list = os.listdir()
                for file_name in filename_list:
                    print(file_name[:-4])
                    file_list = [file_name[:-4]]
                    get_words(file_list)
                    print('----')

def main(argv):
    get_words(argv)

if __name__ == "__main__":
    main(sys.argv[1:])
