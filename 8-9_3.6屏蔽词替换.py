import re
with open('8-9_屏蔽词.txt', encoding='utf-8') as f:
    b_words = f.read()
    block_words = '|'.join(b_words.split())                        # 草泥替换了马留下来了
    print(block_words)
words = input('输入一段文字：')
words_blocked = re.sub(block_words, '****', words, flags=re.I)     # re的用法完全从网上抄的
print(words_blocked)




