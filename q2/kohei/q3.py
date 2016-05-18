'''
N = input()
if N.count("@") == 1:
	first, second  = N.split("@")
	if second.count(".") >= 1:
		print("This is Address")
	else:
		print("This is not Address")

else:
	print("This is not Address")
'''

import re
N = input()
if re.match("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+",N):
	print("This is address")
else:
	print("This is not adress")
