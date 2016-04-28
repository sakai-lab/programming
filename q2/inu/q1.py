# for q1
member = {}

for line in open('../data.txt', 'r'):
  name, height, weight = line.split(',')
  member[name] = { "height": float(height), "weight": float(weight) }

def bmi_calculator(name, member_list):
  if name in member_list:
    person = member_list[name]
    weight, height = person["weight"], person["height"]
    return weight / ((height/100)**2)
  else:
    return "Invalid name"
