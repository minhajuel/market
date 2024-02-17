# Mendefinisikan harga buah
price_apel = 10000
price_jeruk = 15000
price_anggur = 20000

# Mendifinisikan stock buah
stock_apel = 5
stock_jeruk = 10
stock_anggur = 7


while True:
    # meminta input jumlah apel yang dibeli kepada user
    while True:
        n_apel = int(input('Masukkan jumlah apel: '))
        if n_apel > stock_apel:
            print(f'Jumlah pesanan tidak terpenuhi. Stock apel sisa {stock_apel}')
        else:
            break
        
    # meminta input jumlah jeruk yang dibeli kepada user
    while True:
        n_jeruk = int(input('Masukkan jumlah jeruk: '))
        if n_jeruk > stock_jeruk:
            print(f'Jumlah pesanan tidak terpenuhi. Stock jeruk sisa {stock_jeruk}')
        else:
            break

    # meminta input jumlah anggur yang dibeli kepada user
    while True:
        n_anggur = int(input('Masukkan jumlah anggur: '))
        if n_anggur > stock_anggur:
            print(f'Jumlah pesanan tidak terpenuhi. Stock anggur sisa {stock_anggur}')
        else:
            break

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

    # Melakukan pembayaran
    while True:
        pembayaran = int(input("Masukkan jumlah uang: "))
        if pembayaran >= total:
            print('Terima Kasih')
            print(f'Kembalian anda sebesar: {pembayaran - total}')
            break
        else:
            print(f'Uang yang anda masukkan kurang: {total - pembayaran}')

    # update stock
    stock_apel -= n_apel
    stock_jeruk -= n_jeruk
    stock_anggur -= n_anggur

    # konfirmasi belanja ulang
    konfirmasi = input('Apakah anda mau berbelanja lagi? ')
    if konfirmasi == "no":
        break
    