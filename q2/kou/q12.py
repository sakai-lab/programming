# for q1
f=open('../data.txt','r')
member={}

for line in f:
    s=line.split(',')
    member[s[0]]={"height":float(s[1]), "weight":float(s[2])}

"""
print(member["sato"]["weight"])
print(member["uchimura"]["weight"])
"""

print("name list")
for w in member.keys():
    print(w)

#for q2
def BMI(m):
    return m["weight"]/((m["height"]/100)**2)

print("BMI calculation: name? :",end="")
name=input()
if name in member:
    print(BMI(member[name]))
else:
    print("No data")
