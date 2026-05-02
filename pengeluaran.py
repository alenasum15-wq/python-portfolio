import csv

def tambah_pengeluaran():
    print("=== Pencatatan Pengeluaran Kost ===")
    
    tanggal = input("Masukkan tanggal (dd/mm/yyyy): ")
    nama = input("Masukkan nama pengeluaran: ")
    jumlah = input("Masukkan jumlah (Rp): ")
    
    with open("pengeluaran_kost.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, nama, jumlah])
    
    print(f"✅ {nama} sebesar Rp{jumlah} berhasil disimpan!")

tambah_pengeluaran()
