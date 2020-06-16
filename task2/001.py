# jumlah karakter
# katas = input("masukkan kata:")
# hitung = len(katas)
# print("kata %s memiliki panjang karakter: %i " % (katas, hitung))
class Sum:
    @staticmethod
    def jumlah_assert(katas):
        assert katas == input("masukkan kata:")
        len(katas)


if __name__ == "__main__":
    hitung = Sum.jumlah_assert(katas=2)
    print("kata %s memiliki panjang karakter: %i " % ())
