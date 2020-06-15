# Trim

def Trims(args1, args2=10, args3='...'):

    text = args1
    return text[0:args2] + args3


tulisanPanjang = Trims("ini adalah tulisan yang sangat panjang", 8)
print(tulisanPanjang)
