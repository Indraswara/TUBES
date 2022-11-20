import os

pengeluaran = {}
rerun = []

def init_object():
  f = open('pengeluaran.txt', 'r+')
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
      pengeluaran.update({temp[0]: args})
    i += 1
  if os.stat("pengeluaran.txt").st_size == 0:
    f.write('id,besar_pengeluaran,jenis_pengeluaran,')
  
  f.close()

def obj_to_list():
  ans = []
  if len(rerun) > 0:
    ans = [','.join(rerun[0])]
  else:
    ans = ['id,besar_pengeluaran,jenis_pengeluaran,\n']

  for val in pengeluaran:
    temp = [
      val,pengeluaran[val]['besar_pengeluaran'],
      str(pengeluaran[val]['jenis_pengeluaran'])
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
    ans = ['id,besar_pengeluaran,jenis_pengeluaran,\n']

  for val in pengeluaran:
    temp = [val,pengeluaran[val]['besar_pengeluaran'],str(pengeluaran[val]['jenis_pengeluaran'])]
    temp = ','.join(temp) + '\n'
    ans.append(temp)
    
  temp = ans[0]
  ans.pop(0)
  ans.sort()
  ans = [temp] + ans
  return ''.join(ans)

def update_pengeluaran(id, args):
  for key, val in args.items():

    if pengeluaran.get(id):
      pengeluaran[id].update({key: val})
    else:
      pengeluaran.update({id: {}})
      pengeluaran[id].update({key: val})
        
  f = open('pengeluaran.txt', 'w')
  ans = obj_to_list()
  f.write(ans)
  f.close()

def delete_pengeluaran(id, args):
  for key, val in args.items():
    
    if pengeluaran.get(id):
      pengeluaran[id].update({key: val})
    else:
      pengeluaran.update({id: {}})
      pengeluaran[id].update({key: val})
      
  f = open('pengeluaran.txt', 'w')
  ans = del_obj()
  f.write(ans)
  f.close()

def reset_pengeluaran(): 
  f = open('pengeluaran.txt', 'r+')
  lines = f.readlines()
  f.seek(0)
  for line in lines: 
    if line != lines[0]:
      f.truncate()
  pengeluaran = {}
  f.close()
  return pengeluaran

def balance_return(id):
  saldo = pengeluaran[id]["besar_pengeluaran"]
  return saldo

def cek_pengeluaran():
  return pengeluaran