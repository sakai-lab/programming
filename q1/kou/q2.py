import sys

#文字列内の文字が全て数字であるかを判定
def all_num(s):
	#文字列が空である場合にもエラー
	if len(s)==0: return False

	for v in s:
		if v<='0' or '9'<=v:
			return False

	return  True

if __name__ == "__main__":
	argvs=sys.argv
	argc=len(argvs)

	valid=True

	#引数は2つじゃないとダメ
	if argc==2:
		ipv4=argvs[1]
		#受け取った文字列を'.'で分割
		nums=ipv4.split('.')
		if len(nums)==4:
			for elem in nums:
				if all_num(elem):
					num=int(elem)
					#それぞれの値に対して0~255の間に収まっているかを判定
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
	print(ans,"for IPv4 Address")
