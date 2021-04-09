angka = []
total = 0

#memasukkan data
banyak = int(input("Masukkan banyak bilangan Anda : "))

for a in range(0, banyak):
    temp = int(input("Masukkan nilai ke-%d Anda : " %(a+1)))
    angka.append(temp)
    total += angka[a]
    rata_bilangan = total / banyak
print("Rata-rata", banyak, "bilangan Anda adalah", round(rata_bilangan,2))
