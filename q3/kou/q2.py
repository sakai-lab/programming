'''
ひらがなと半角スペースの文字列に関して俳句の形を判定する正規表現
(字余り、字足らずは禁止)
'''

import re

print('string > ',end="")
s=input()

p=re.compile('^([ぁ-ん]{5}\x20[ぁ-ん]{7}\x20[ぁ-ん]{5})$')
m=p.match(s)

if m:
    print(m.group(),'is Haiku')
else:
    print('Not Haiku')
