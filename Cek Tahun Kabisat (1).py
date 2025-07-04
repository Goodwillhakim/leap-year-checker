print("=" *41)
print("              Tahun Kabisat")
print("=" *41)

#Pengambilan Data

Tahun = int(input("Masukan Tahun Yang Ingin Di Cek: "))
if Tahun % 4 == 0 and (Tahun % 100 != 0 or Tahun % 400 == 0):
    print (f"{Tahun} Adalah Tahun Kabisat")
