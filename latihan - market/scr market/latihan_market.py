# Mendefinisikan harga buah
price_apel = 10000
price_jeruk = 15000
price_anggur = 20000

# Mendifinisikan stock buah
stock_apel = 5
stock_jeruk = 10
stock_anggur = 7

# Ucapan pembuka
print('Selamat Datang di Pasar Buah!')

# Mendefinisikan validasi input untuk number
def is_number(value):
    try:
        int(value)
        return True
    except:
        return False

# Mendefinisikan fungsi input buah
def inputBuah(stock, price, name = 'Apel'):
    
    # Meminta jumlah buah yang dipesan
    while True:
        qty = input (f'Masukkan jumlah {name}: ')
        # validasi inputan
        if is_number(qty):
            qty = int(qty)
            # Membandingkan ketersediaan buah dengan pesanan
            if qty > stock:
                print(f'Jumlah pesanan tidak terpenuhi, stock {name} sisa {stock}')

            else:
                break
        else:
            print('Masukkan angka!')

    # Menghitung total harga buah
    totalPrice = qty * price
    
    # Update stock buah
    stock -= qty

    return qty, totalPrice, stock
                      
def pembayaran(nominal):
    while True:
        # Meminta input uang pembayaran
        pembayaran = input(f"Masukkan jumlah {nominal}: ")
        # Validasi input
        if is_number(pembayaran):
            pembayaran = int(pembayaran)

            # Menghitung kekurangan atau sisa
            if pembayaran >= nominal:
                print('Terima Kasih')
                print(f'Kembalian anda sebesar: {pembayaran - nominal}')
                break
            else:
                print(f'Uang yang anda masukkan kurang: {nominal - pembayaran}')
        else:
            print("Masukkan angka")
                                      
# Main Program
while True:
    # Hitung harga per buah
    n_apel, total_apel, stock_apel = inputBuah(stock_apel,price_apel, name='Apel')
    n_jeruk,total_jeruk, stock_jeruk = inputBuah(stock_jeruk,price_jeruk, name='Jeruk')
    n_anggur, total_anggur, stock_anggur = inputBuah(stock_anggur,price_anggur, name='Anggur')

    # Menghitung total belanjaan
    total = total_apel + total_jeruk + total_anggur

    # Tampilkan detail belanjaan
    print(f'''Detail Belanjaan
    Apel : {n_apel} x {price_apel} = {total_apel}
    Jeruk : {n_jeruk} x {price_jeruk} = {total_jeruk}
    Anggur : {n_anggur} x {price_anggur} = {total_anggur}

    Total : {total}      
    ''')

    # Melakukan pembayaran
    pembayaran(total)

    # konfirmasi belanja ulang
    konfirmasi = input('Apakah anda mau berbelanja lagi? ')
    if konfirmasi == "no":
        break
    