Total_uang_belanja = float(input("masukan total uang belanja anda: "))
Total_belanja      = float(input("masukan total belanja anda: "))

if Total_belanja < 70000 :
    diskon = 0.1 * Total_belanja 
    total_setelah_diskon = Total_belanja - diskon
    Kembalian = Total_uang_belanja - Total_belanja_setelah_diskon

print("uang kembalian anda : %.2f" %Kembalian)