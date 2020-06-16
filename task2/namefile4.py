# Kabisat
tahuns = int(input("Masukkan tahun: "))

if tahuns % 400 == 0 | tahuns % 100 == 0 | tahuns % 4 == 0:
    print("%i merupakan tahun kabisat" % (tahuns))
else:
    print("%i merupakan bukan tahun kabisat" % (tahuns))
