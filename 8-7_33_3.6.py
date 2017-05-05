# 统计8-7_33scores.txt里每个人的总得分

with open('8-7_33scores.txt', encoding='utf-8') as f:
    list1 = f.readlines()
list2 = [i.split() for i in list1]                                     # 文件内容分割为列表
print(list2)
list3 = [[i[0], str(sum([int(j) for j in i[1:]]))] for i in list2]    # j为i[1:]，也就是每个人的成绩的列表。为方便list4合并成字符串，成绩转化为str
print(list3)                                                           # 也就是说计算总分的功能，一行三层嵌套的列表解析代码就可以搞定...
list4 = list3[:]                                                       # 在list4中调整格式，不改变list3数据
for i in list4:
    i.insert(1, ': ')
    i.append('\n')
list5 = [''.join(i) for i in list4]
print(''.join(list5))
with open('8-7_33out.txt', 'w') as f:
    f.write(''.join(list5))

