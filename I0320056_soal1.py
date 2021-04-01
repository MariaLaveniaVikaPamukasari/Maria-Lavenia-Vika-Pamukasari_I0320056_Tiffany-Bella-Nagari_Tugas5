print(" ")
print("Program untuk menyapa pengunjung hotel")
print(" ")
print("==========================================================")
print("\t\t\t\tHotel 'Mekar Jaya'")
print("Jalan Genting Raya, No. 24C, Mutiara Indah Baru, Jakarta")
print("==========================================================")
nama = input("Silahkan masukkan nama Anda:")
jenis_kelamin = input("Bolehkah kami mengetahui jenis kelamin Anda? (P/L) :").upper()
if jenis_kelamin == "P":
    print("\n\t\tSelamat datang, Saudari", nama, '!')
elif jenis_kelamin == "L":
    print("\n\t\tSelamat datang, Saudara", nama, '!')
else:
    pass
