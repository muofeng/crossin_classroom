# coding:gbk
import os
import chardet
paths = []
dirs = []
files = []
for i, j, k in os.walk('f:\\Users\\ZhangYF\\Desktop\\Python\\practice'):        # 将'每节练习'里的文档拷进'practice'，并用notepad++将8-7_33out.txt转为utf-8，简化了编码环境
    paths.append(i)
    dirs.append(j)
    files.append(k)
key_word = input('请输入关键词:')
file_name = []
file_contents = []
file_notdetect = []
for i in range(len(paths)):
    for j in files[i]:
        if key_word in j:
            file_name.append(j)
        file_path = paths[i]+'\\' + j
        with open(file_path, 'rb') as f:                                      # 以二进制打开
            content1 = f.read()
            result = chardet.detect(content1)                                  # 获取文档编码
            file_code = result['encoding']
        if file_code is None:                                                 # 文档为空或内容无法识别
            file_notdetect.append(j)
        else:
            with open(file_path, encoding=file_code) as f:                    # 用获取的编码打开文档。可以试一下用codecs解决无法打开的问题
                content2 = f.read()
                if key_word in content2:
                    file_contents.append(j)
print('文档名包含关键词：%s' % ', '.join(file_name))
print('文档内容包含关键词：%s' % ', '.join(file_contents))
print('文档内容为空或者无法识别：%s' % ', '.join(file_notdetect))






