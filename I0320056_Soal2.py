print(" ")
print("\t\t\tProgram grading nilai")
print(" ")
print("=======================================")
nama = input("Silahkan masukkan nama Anda:")
nilai = int(input("Silahkan masukkan nilai Anda:"))
if nilai < 60:
    str(print("Halo", nama, "!", "Nilai anda setelah dikonversi menjadi E"))
elif 60 <= nilai <= 64:
    str(print("Halo", nama, "!", "Nilai anda setelah dikonversi menjadi C"))
elif 65 <= nilai <= 69:
    str(print("Halo", nama, "!", "Nilai anda setelah dikonversi menjadi C+"))
elif 70 <= nilai <= 74:
    str(print("Halo", nama, "!", "Nilai anda setelah dikonversi menjadi B"))
elif 75 <= nilai <= 79:
    str(print("Halo", nama, "!", "Nilai anda setelah dikonversi menjadi B+"))
elif 80 <= nilai <= 84:
    str(print("Halo", nama, "!", "Nilai anda setelah dikonversi menjadi A-"))
elif 85 <= nilai <= 100:
    str(print("Halo", nama, "!", "Nilai anda setelah dikonversi menjadi A"))
else:
    pass
