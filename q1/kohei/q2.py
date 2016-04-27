N = list(input().split("."))

if len(N) != 4:
	N[:] = "Falese"
else:
	for i in range(4):
		if 0 <= int(N[i]) <= 255:
			N[i] = "True"
		else:
			N[i] = "False"
			
if N.count("True") == 4:
	print("IPv4 address")
else:
	print("Not IPv4 address")