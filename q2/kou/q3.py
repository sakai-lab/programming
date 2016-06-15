import re

print("mail address > ",end="")
address=input()
print(address)

# 全体が一致しているかどうかだけ知りたい
p=re.compile('^([a-zA-Z0-9.-]+@[a-zA-Z0-9-]+(.[a-zA-Z0-9-]+)+)$')
m=p.match(address)

if m:
    print(m.group(),'is valid')
else:
    print('Invalid')
