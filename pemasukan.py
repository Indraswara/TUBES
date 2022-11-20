import os

pemasukan = {}
rerun = []

def init_object():
  f = open('pemasukan.txt', 'r+')
  i = 0
  init = []
  for x in f:
    temp = x.split(',')
    rerun.append(temp)
    if i == 0:
      init = temp
    else:
      temp[-1] = temp[-1]
      temp[-2] = temp[-2]

      args = {
        init[0]: temp[0], 
        init[1]: temp[1], 
        init[2]: temp[2]

      }
      pemasukan.update({temp[0]: args})
    i += 1
  if os.stat("pemasukan.txt").st_size == 0:
    f.write('id,besar_pemasukan,jenis_pemasukan,')

  f.close()

def obj_to_list():
  ans = []
  if len(rerun) > 0:
    ans = [','.join(rerun[0])]
  else:
    ans = ['id,besar_pemasukan,jenis_pemasukan,\n']
  
  for val in pemasukan:
    temp = [
      val, pemasukan[val]['besar_pemasukan'],
      str(pemasukan[val]['jenis_pemasukan']),
      ]
    temp = ','.join(temp) +',\n'
    ans.append(temp)
  
  # print('ini ans',ans)
  temp = ans[0]
  ans.pop(0)
  ans.sort()
  ans = [temp] + ans
  return ''.join(ans)

def del_obj():
  ans = []
  if len(rerun) > 0:
    ans = [','.join(rerun[0])]
  else:
    ans = ['id,besar_pemasukan,jenis_pemasukan,\n']

  for val in pemasukan:
    temp = [val,pemasukan[val]['besar_pemasukan'],str(pemasukan[val]['jenis_pemasukan'])]
    temp = ','.join(temp) + ',\n'
    ans.append(temp)
  
  temp = ans[0]
  ans.pop(0)
  ans.sort()
  ans = [temp] + ans
  return ''.join(ans)

def update_pemasukan(id, args):
  for key, val in args.items():

    if pemasukan.get(id):
      pemasukan[id].update({key: val})
    else:
      pemasukan.update({id: {}})
      pemasukan[id].update({key: val})

  f = open('pemasukan.txt', 'w')
  ans = obj_to_list()
  f.write(ans)
  f.close()

def delete_pemasukan(id, args):
  for key, val in args.items():
    
    if pemasukan.get(id):
      pemasukan[id].update({key: val})
    else:
      pemasukan.update({id: {}})
      pemasukan[id].update({key: val})
      
  f = open('pemasukan.txt', 'w')
  ans = del_obj()
  f.write(ans)
  f.close()

def reset_pemasukan(): 
  f = open('pemasukan.txt', 'r+')
  lines = f.readlines()
  f.seek(0)
  for line in lines: 
    if line != lines[0]:
      f.truncate()
  pemasukan = {}
  f.close()
  return pemasukan
  
def balance_return(id):
  saldo = pemasukan[id]["besar_pemasukan"]
  return saldo

def cek_pemasukan():
  return pemasukan