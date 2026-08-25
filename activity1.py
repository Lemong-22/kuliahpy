panjang_taman = 12
lebar_taman = 10
panjang_rumah = 8
lebar_rumah = 5

luas_taman = panjang_taman * lebar_taman
luas_rumah = panjang_rumah * lebar_rumah

luas_rumput = luas_taman - luas_rumah
total_biaya=luas_rumput*1000

print(f'total biaya potong rumput adalah Rp {total_biaya}')