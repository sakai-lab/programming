import sys

#文字列内の文字が全て数字であるかを判定
def all_num(s):
	ret=True
	for v in s:
		if v<='0' or '9'<=v:
			ret=False
	return ret

if __name__ == "__main__":
	argvs=sys.argv
	argc=len(argvs)

	valid=True

	#引数は2つじゃないとダメ
	if argc==2:
		ipv4=argvs[1]
		nums=ipv4.split('.')
		if len(nums)==4:
			for elem in nums:
				if all_num(elem):
					num=int(elem)
					if num<0 or 255<num:
						valid=False
						break
				else:
					valid=False
					break
		else:
			valid=False
	else:
		valid=False

	#output
	ans="Invalid"
	if valid:
		ans="Valid"
	print(ans,"for IPv4")
