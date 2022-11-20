import wallet
import pengeluaran
import pemasukan
import exsaldo
import os

balance = 0.0000

print("Welcome to Sys Financial Manager!")

print("""
1) Pemasukan
2) Pengeluaran
3) Cek Pemasukan
4) Cek Pengeluaran
5) Hapus Pemasukan 
6) Hapus Pengeluaran
7) Riwayat Saldo
8) Reset
9) Exit
""")
# Cek Data
pemasukan.init_object()
pengeluaran.init_object()
exsaldo.init_object()

isRun = True
while isRun:

  balance = wallet.read_balance()
  print(f"Saldo: {str(balance)}")
  option = int(input("Pilih opsi: "))
  if option == 1:
    id = input("Pemasukan ke: ")
    besar_pemasukan = input("Besar pemasukan: ")
    jenis_pemasukan = input("Jenis pemasukan: ") + ""
    args = {
      "besar_pemasukan" : besar_pemasukan,
      "jenis_pemasukan" : jenis_pemasukan,
    }
    pemasukan.update_pemasukan(id, args)
    balance = wallet.read_balance()
    balance += float(besar_pemasukan)
    wallet.update_balance(balance)
    print()

  elif option == 2:
    id = input("Pengeluaran ke: ")
    besar_pengeluaran = input("Besar pengeluaran: ")
    jenis_pengeluaran = input("Jenis pengeluaran: ") + ""
    args = {
      "besar_pengeluaran" : besar_pengeluaran,
      "jenis_pengeluaran" : jenis_pengeluaran,
    }
    pengeluaran.update_pengeluaran(id, args)
    balance = float(wallet.read_balance())
    balance -= float(besar_pengeluaran) 
    wallet.update_balance(balance)
    print()

  #elif option == 3:
    #balance = wallet.read_balance()
    #if balance == None:
      #balance = 0    
    #print(f"Saldo: {str(balance)}")
    #print()

  elif option == 3:
    data = pemasukan.cek_pemasukan()
    print("=" * 74)
    print("||" + "DAFTAR PEMASUKAN".center(70) + "||")
    print("||" + "-" * 70 + "||")
    print("||" + "id".center(10) + "besar_pemasukan".center(30) + "jenis_pemasukan".center(30) + "||")
    print("||" + "-" * 70 + "||")
    for x in data:
      print("||" + str(x).center(15) + "\t".expandtabs(3) + pemasukan.pemasukan[x]['besar_pemasukan'].ljust(30) + pemasukan.pemasukan[x]['jenis_pemasukan'].ljust(22) + "||")
      print("=" * 74)
  
  elif option == 4:
    data = pengeluaran.cek_pengeluaran()
    print("=" * 74)
    print("||" + "DAFTAR PENGELUARAN".center(70) + "||")
    print("||" + "-" * 70 + "||")
    print("||" + "id".center(10) + "besar_pengeluaran".center(30) + "jenis_pengeluaran".center(30) + "||")
    print("||" + "-" * 70 + "||")
    for x in data:
      print("||" + str(x).center(15) + "\t".expandtabs(3) + pengeluaran.pengeluaran[x]['besar_pengeluaran'].ljust(30) + pengeluaran.pengeluaran[x]['jenis_pengeluaran'].ljust(22) + "||")
      print("=" * 74)

  elif option == 5:
    id = input("Pemasukan ke: ")
    args = {
      "besar_pemasukan": '',
      "jenis_pemasukan": '' + ""
    }
    saldo_return = float(pemasukan.balance_return(id))
    saldo = float(wallet.read_balance())
    if saldo == None:
      saldo = 0
    saldo -= saldo_return
    wallet.update_balance(saldo)
    pemasukan.delete_pemasukan(id, args)
    print()

  elif option == 6:
    id = input("Pengeluaran ke: ")
    args = {
      "besar_pengeluaran": '',
      "jenis_pengeluaran": '' + ""
    }
    saldo_return = float(pengeluaran.balance_return(id))
    saldo = float(wallet.read_balance())
    if saldo == None:
      saldo = 0
    saldo += saldo_return
    wallet.update_balance(saldo)
    pengeluaran.delete_pengeluaran(id, args)
    print()

  elif option == 7:
    data = exsaldo.cek_exsaldo()
    print("=" * 74)
    print("||" + "RIWAYAT SALDO".center(70) + "||")
    print("||" + "-" * 70 + "||")
    print("||" + "id".center(10) + "besar_sisa_saldo".center(30) + "bulan_sisa_saldo".center(30) + "||")
    print("||" + "-" * 70 + "||")
    for x in data:
      print("||" + str(x).center(15) + "\t".expandtabs(3) + exsaldo.exsaldo[x]['besar_exsaldo'].ljust(30) + exsaldo.exsaldo[x]['bulan_exsaldo'].ljust(22) + "||")
      print("=" * 74)

  elif option == 8: 
    status = True
    while status:
      print("Apa anda yakin?(Y/N)")
      acceptance = input("--> ") 
      if acceptance == 'Y' or acceptance == 'y':
        id = input("Pencatatan ke:  ")
        balance = str(wallet.read_balance())
        besar_exsaldo = balance
        bulan_exsaldo = input("Bulan apa? ") + ""
        args = { 
          "besar_exsaldo" : besar_exsaldo,
          "bulan_exsaldo" : bulan_exsaldo,
        }
        exsaldo.update_exsaldo(id, args)
        print()

        pemasukan.reset_pemasukan()
        pengeluaran.reset_pengeluaran()
        #wallet.update_balance(0)
        status = False

      elif acceptance == 'N' or acceptance == 'n': 
        status = False
  
  elif option == 9:
    isRun = False