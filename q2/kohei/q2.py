def BMI(dic,name):

	new_height = float(dic[name]["height"])/100
	new_weight = float(dic[name]["weight"])
	print((new_weight)/((new_height)*(new_height)))




if __name__ == '__main__':
	member = {}
	for line in open('data.txt', 'r'):
		data = line.split(",")
		member[data[0]] = {
			"height":data[1],
			"weight":data[2]
		}

	BMI(member,"sato")
