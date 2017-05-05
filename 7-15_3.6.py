import random
import string

letters = list(string.ascii_letters)
coupons = []
while len(coupons) < 200:
    random.shuffle(letters)                 # 用sample更简单
    code_list = letters[:8]
    code = ''.join(code_list)
    if code not in coupons:
        coupons.append(code)
print(coupons)
print(len(coupons))                         # 看coupons里面的数目是不是正确


