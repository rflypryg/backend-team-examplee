def keliling_persegi(panjang,lebar):
    keliling = 2 * (panjang + lebar)
    return keliling

def luas_persegi(panjang,lebar):
    luas = panjang * lebar 
    return luas

panjang = float (input ("Masukan panjang persegi: "))
lebar = float (input ("Masukan lebar persegi: "))
keliling = keliling_persegi(panjang,lebar)
print ("keliling persegi panjang : ", keliling)
luas = luas_persegi(panjang,lebar)
print ("luas persegi panjang: ", luas)