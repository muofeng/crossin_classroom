score = [['张三', 89, 78, 91], ['李四', 99, 87], ['王五', 49, 55, 78]]
print(score)
score1 = sorted([[x[0], (x[1]+x[2]+x[3])/3] for x in score if len(x) == 4], key=lambda y: y[1], reverse=True)  #用y是不想和前面x的搞混；求平均分可以用sum(x[1:])/3
print(score1)

