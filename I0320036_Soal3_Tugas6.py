#range
batas_bawah = 10
batas_atas = 24

#proses penentuan bilangan prima atau bukan
for x in range(batas_bawah, batas_atas+1):
    if x > 0:
        for y in range(2, x):
            if (x %y) == 0:
                print(x, "bukan prima")
                break
        else:
            print(x, "adalah bilangan prima")