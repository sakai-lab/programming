'''
入力された文字列(.と数字の連続)が
IPv4で定義された範囲のIPアドレス(***.***.***.***)
になりえるかどうか判定するプログラムを書け
'''

import re

print('IP Address > ',end="")
address=input()

p=re.compile('^(([0-9]|[0-9][0-9]|[01][0-9][0-9]|2[0-4][0-9]|25[0-5])(.([0-9]|[0-9][0-9]|[01][0-9][0-9]|2[0-4][0-9]|25[0-5])){3})$')
m=p.match(address)

if m:
    print(m.group(),'is valid')
else:
    print('Invalid')
