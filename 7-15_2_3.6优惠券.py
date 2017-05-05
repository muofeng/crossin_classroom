import random
import string

letters = list(string.ascii_letters)
coupons = []
while len(coupons) < 200:
    code = ''.join(random.sample(letters, 8))               # 明明有sample题目却只提示shuffle
    if code not in coupons:
        coupons.append(code)
print(coupons)
print(len(coupons))                                         # 看coupons里面的数目是不是正确
