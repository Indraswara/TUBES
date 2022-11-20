import os

exsaldo = {}
rerun = []

def init_object():
  f = open('exsaldo.txt', 'r+')
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
      exsaldo.update({temp[0]: args})
    i += 1
  if os.stat("exsaldo.txt").st_size == 0:
    f.write('id,besar_exsaldo,bulan_exsaldo,')

  f.close()

def obj_to_list():
  ans = []
  if len(rerun) > 0:
    ans = [','.join(rerun[0])]
  else:
    ans = ['id,besar_exsaldo,bulan_exsaldo,\n']
  
  for val in exsaldo:
    temp = [
      val, exsaldo[val]['besar_exsaldo'],
      str(exsaldo[val]['bulan_exsaldo']),
      ]
    temp = ','.join(temp) +',\n'
    ans.append(temp)
  
  # print('ini ans',ans)
  temp = ans[0]
  ans.pop(0)
  ans.sort()
  ans = [temp] + ans
  return ''.join(ans)

def update_exsaldo(id, args):
  for key, val in args.items():

    if exsaldo.get(id):
      exsaldo[id].update({key: val})
    else:
      exsaldo.update({id: {}})
      exsaldo[id].update({key: val})

  f = open('exsaldo.txt', 'w')
  ans = obj_to_list()
  f.write(ans)
  f.close()

def cek_exsaldo():
  return exsaldo