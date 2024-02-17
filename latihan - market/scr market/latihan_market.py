# Mendefinisikan harga buah
price_apel = 10000
price_jeruk = 15000
price_anggur = 20000


# meminta input jumlah buah kepada user
n_apel = int(input('Masukkan jumlah apel: '))
n_jeruk = int(input('Masukkan jumlah jeruk: '))
n_anggur = int(input('Masukkan jumlah anggur: '))

# Menghitung total belanjaan per buah
total_apel = n_apel * price_apel
total_jeruk = n_jeruk * price_jeruk
total_anggur = n_anggur * price_anggur

# Menghitung total belanjaan
total = total_apel + total_jeruk + total_anggur

#Show
print(f'''Detail Belanjaan
Apel : {n_apel} x {price_apel} = {total_apel}
Jeruk : {n_jeruk} x {price_jeruk} = {total_jeruk}
Anggur : {n_anggur} x {price_anggur} = {total_anggur}

Total : {total}      
''')
