str_input = raw_input()

def ipv4_checker(seq):
  num_lis = map(int, seq.split("."))
  if seq.count('.') != 3: return False
  if len(num_lis) != 5: return False

  for i in num_lis:
    if !(0 <= i <= 255):
      return False

  return True

print ipv4_checker(str_input)
