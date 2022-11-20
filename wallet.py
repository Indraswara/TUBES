def init_file():
  balance = 0
  f = open("balance.txt", "r+")
  for line in f.readlines():
    balance += float(line)
  f.close()
  return balance

def update_balance(option_1):
  f = open("balance.txt", "w")
  f.write(str(option_1))
  f.close

def read_balance():
  balance = init_file()
  return balance