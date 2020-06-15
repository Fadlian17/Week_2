# TrimWords
def TrimsWords(args1, args2=5):
    text = args1.split()
    tewords = list(text[0:args2])
    stri1 = '  '.join(tewords)
    return stri1


tulisanPanjang = TrimsWords("ini adalah tulisan yang sangat panjang", 3)

print(tulisanPanjang)
