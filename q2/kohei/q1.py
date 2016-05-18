'''
member = {{"name":"sato","height":"172.5","weight":"66.5"},
{"name":"suzuki","height":"164.7","weight":"62.5"},
{"name":"kimura","height":"154.6","weight":"50.8"},
{"name":"uchimura","height":"187.3","weight":"81.0"}
}
'''

member = {}
b = {}

for line in open('data.txt', 'r'):
	#print(line)
	data = line.split(",")
	'''dic = {
		"name":data[0],
		"height":data[1],
		"weight":data[2]
	}'''
	member[data[0]] = {
		"height":data[1],
		"weight":data[2]
	}

print(member["sato"]["height"])

