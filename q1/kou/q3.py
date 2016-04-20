dict={
	'sakai' : 'tetsuya',
	'nakajima' : 'tatsuo',
	'washizaki' :'hironori'
}

print('input? ',end='')
s=input()

if s in dict:
	print(dict[s])
else:
	print('Invalid Input.')
