class Code:
    @staticmethod
    def satu1():
        katas = input("masukkan kata:")
        hitung = len(katas)
        print("kata %s memiliki panjang karakter: %i " % (katas, hitung))

    @staticmethod
    def dua2():
        score = int(input("Masukkan nilai anda = "))
        if score >= 90:

            print("grade A")

        elif score >= 80 and score < 90:

            print("grade B")

        elif score >= 70 and score < 80:

            print("grade C")

        elif score >= 60 and score < 70:

            print("grade D")

        elif score < 60:

            print("grade E")
        else:
            print("No Grade")

    @staticmethod
    def tiga3():
        n = int(input("Masukkan sebuah bilangan: "))
        if n % 2 == 0:
            print("Bilangan {} adalah genap.".format(n))
        else:
            print("Bilangan {} adalah ganjil.".format(n))

    @staticmethod
    def empat4():
        tahun = int(input("Masukkan Data tahun: "))
        if (tahun % 4) == 0:
            if (tahun % 100) == 0:
                if (tahun % 400) == 0:
                    print("{0} merupakan tahun kabisat".format(tahun))
                else:
                    print("{0} bukan merupakan tahun kabisat".format(tahun))
            else:
                print("{0} merupakan tahun kabisat".format(tahun))
        else:
            print("{0} bukan merupakan tahun kabisat".format(tahun))

    @staticmethod
    def lima5():
        film = int(input("Rating sebuah Film = "))

        if (film >= 21):
            print("Khusus DEWASA")

        elif (film >= 13):
            print("Khusus Remaja")

        elif (film >= 9):
            print("Bimbingan Orang tua")

        elif (film < 9):
            print("Semua Usia")

    @staticmethod
    def enam6():
        first = int(input("Input pertama : "))
        second = int(input("Input kedua : "))

        for output in range(first, second+1):
            print(output)

    @staticmethod
    def tujuh7():
        batasan = int(input('Masukkan Batasan Angka : '))

        for a in range(2, batasan, 1):
            mod = 1
            for b in range(2, a, 1):
                if (a % b == 0):
                    mod = 0

            if (mod == 1):
                print(a)

    @staticmethod
    def delapan8():
        def cetak(a, b):
            for item in range(a, b):
                if item % 2 == 0:
                    if item % 5 == 0:
                        if item % 100 == 0:
                            print("%i. Genap Kelipatan Seratus" % (item))
                        else:
                            print("%i. Genap Kelipatan Lima" % (item))
                    else:
                        print("%i. Genap" % (item))
                else:
                    if item % 5 == 0:
                        print("%i. Ganjil Kelipatan Lima" % (item))
                    else:
                        print("%i. Ganjil" % (item))

        cetak(1, 200)

    @staticmethod
    def sembilan9():
        sentence = 'saya ingin makan nasi goreng'
        string = sentence.split()
        print(' '.join(string[::-1]))

    @staticmethod
    def sepuluh10():
        stuff = ['Meja', 'Buku', 'Topi', 'Baju', 'Kayu']
        stuff.insert(5, "Celana")
        stuff.insert(0, "Handuk")
        print(stuff)


if __name__ == "__main__":
    Code.satu1
    Code.dua2
    Code.tiga3
    Code.empat4
    Code.lima5
    Code.enam6
    Code.tujuh7
    Code.delapan8
    Code.sembilan9
    Code.sepuluh10
    print("Result OK")
