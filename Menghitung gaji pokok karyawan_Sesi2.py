gaji_pokok            = float(input("masukan gaji pokok karyawan : "))
uang_transport_harian = float(input("masukan uang tansport harian karyawan :"))
uang_makan_harian     = float(input("masukan uang makan harian karyawan : "))
tunjangan_jabatan     = float(input("masukan tunjangan jabatan karyawan : "))
honor_lembur          = float(input("masukan honor lembur karyawan : "))

total_gaji = gaji_pokok + uang_transport_harian + uang_makan_harian + tunjangan_jabatan + honor_lembur
print("total gaji :%.0f" %total_gaji)