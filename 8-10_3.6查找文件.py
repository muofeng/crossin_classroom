# coding:gbk
import os
import chardet
paths = []
dirs = []
files = []
for i, j, k in os.walk('f:\\Users\\ZhangYF\\Desktop\\Python\\practice'):        # ��'ÿ����ϰ'����ĵ�����'practice'������notepad++��8-7_33out.txtתΪutf-8�����˱��뻷��
    paths.append(i)
    dirs.append(j)
    files.append(k)
key_word = input('������ؼ���:')
file_name = []
file_contents = []
file_notdetect = []
for i in range(len(paths)):
    for j in files[i]:
        if key_word in j:
            file_name.append(j)
        file_path = paths[i]+'\\' + j
        with open(file_path, 'rb') as f:                                      # �Զ����ƴ�
            content1 = f.read()
            result = chardet.detect(content1)                                  # ��ȡ�ĵ�����
            file_code = result['encoding']
        if file_code is None:                                                 # �ĵ�Ϊ�ջ������޷�ʶ��
            file_notdetect.append(j)
        else:
            with open(file_path, encoding=file_code) as f:                    # �û�ȡ�ı�����ĵ���������һ����codecs����޷��򿪵�����
                content2 = f.read()
                if key_word in content2:
                    file_contents.append(j)
print('�ĵ��������ؼ��ʣ�%s' % ', '.join(file_name))
print('�ĵ����ݰ����ؼ��ʣ�%s' % ', '.join(file_contents))
print('�ĵ�����Ϊ�ջ����޷�ʶ��%s' % ', '.join(file_notdetect))






